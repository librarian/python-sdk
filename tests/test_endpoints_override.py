from concurrent import futures
from unittest.mock import Mock, patch

import grpc
import pytest

from nebius.vpc.v1.network_service_pb2 import (
    ListNetworksRequest,
    ListNetworksResponse,
)
from nebius.vpc.v1.network_service_pb2_grpc import (
    NetworkServiceStub,
    add_NetworkServiceServicer_to_server,
)
import nebius.vpc.v1.network_service_pb2 as network_service_pb2
from nebiusai import SDK
from nebiusai._channels import Channels

INSECURE_SERVICE_PORT = "50051"
SECURE_SERVICE_PORT = "50052"
SERVICE_ADDR = "localhost"


class VPCServiceMock:

    def __init__(self):
        self.Get = Mock()
        self.GetByName = Mock()
        self.Create = Mock()
        self.Update = Mock()
        self.Delete = Mock()
        self.ListSubnets = Mock()
        self.ListSecurityGroups = Mock()
        self.ListRouteTables = Mock()
        self.ListOperations = Mock()
        self.Move = Mock()

    def List(self, _, context):
        context.set_code(grpc.StatusCode.OK)
        return ListNetworksResponse()


def grpc_server():
    service = VPCServiceMock()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:" + INSECURE_SERVICE_PORT)
    server.add_secure_port("[::]:" + SECURE_SERVICE_PORT, server_credentials=grpc.local_server_credentials())
    add_NetworkServiceServicer_to_server(service, server)
    server.start()
    return server


@pytest.fixture
def mock_channel():
    with patch.multiple(
        Channels,
        _get_creds=lambda self, endpoint: grpc.local_channel_credentials(),
        endpoints=lambda self: {"vpc": f"{SERVICE_ADDR}:{INSECURE_SERVICE_PORT}"},
    ) as channel_patch:
        yield channel_patch


@pytest.mark.parametrize(["port", "insecure"], [(SECURE_SERVICE_PORT, False), (INSECURE_SERVICE_PORT, True)])
def test_we_can_override_endpoint_for_client(port: str, insecure: bool, mock_channel):
    # given
    grpc_server()
    sdk = SDK()
    # when
    network_client = sdk.client(
        network_service_pb2, NetworkServiceStub, endpoint=f"localhost:{port}", insecure=insecure
    )
    # then
    assert isinstance(network_client.List(ListNetworksRequest(parent_id="test")), ListNetworksResponse)


@pytest.mark.parametrize(["port", "insecure"], [(SECURE_SERVICE_PORT, False), (INSECURE_SERVICE_PORT, True)])
def test_override_by_client_is_prior(port: str, insecure: bool, mock_channel):
    # given
    grpc_server()
    sdk = SDK(endpoints={"vpc": "nonlocal-123:12323"})
    # when
    network_client = sdk.client(
        network_service_pb2, NetworkServiceStub, endpoint=f"localhost:{port}", insecure=insecure
    )
    # then
    assert isinstance(network_client.List(ListNetworksRequest(parent_id="test")), ListNetworksResponse)
