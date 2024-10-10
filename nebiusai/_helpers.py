# -*- coding: utf-8 -*-
from typing import TYPE_CHECKING, Optional

from nebius.iam.v1.service_account_service_pb2 import ListServiceAccountRequest
from nebius.iam.v1.service_account_service_pb2_grpc import (
    ServiceAccountServiceStub,
)
from nebius.vpc.v1.network_service_pb2 import ListNetworksRequest
from nebius.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from nebius.vpc.v1.subnet_service_pb2 import ListSubnetsRequest
from nebius.vpc.v1.subnet_service_pb2_grpc import SubnetServiceStub
import nebius.vpc.v1.network_service_pb2 as network_service_pb2
import nebius.vpc.v1.subnet_service_pb2 as subnet_service_pb2
import nebius.iam.v1.service_account_service_pb2 as service_account_service_pb2

if TYPE_CHECKING:
    from nebiusai._sdk import SDK


class Helpers:
    def __init__(self, sdk: "SDK"):
        self.sdk = sdk

    def find_service_account_id(self, parent_id: str) -> str:
        """
        Get service account id in case the folder has the only one service account

        :param parent_id: ID of the folder
        :return ID of the service account
        """
        service = self.sdk.client(service_account_service_pb2, ServiceAccountServiceStub)
        service_accounts = service.List(ListServiceAccountRequest(parent_id=parent_id)).items
        if len(service_accounts) == 1:
            return service_accounts[0].id
        if len(service_accounts) == 0:
            raise RuntimeError(f"There are no service accounts in folder {parent_id}, please create it.")
        raise RuntimeError(f"There are more than one service account in folder {parent_id}, please specify it")

    def find_network_id(self, parent_id: str) -> str:
        """
        Get ID of the first network in folder

        :param parent_id: ID of the folder
        :return ID of the network
        """
        networks = self.sdk.client(network_service_pb2, NetworkServiceStub).List(ListNetworksRequest(parent_id=parent_id)).items
        if not networks:
            raise RuntimeError(f"No networks in folder: {parent_id}")
        if len(networks) > 1:
            raise RuntimeError("There are more than one network in folder {parent_id}, please specify it")
        return networks[0].metadata.id

    def find_subnet_id(self, parent_id: str, network_id: Optional[str] = None) -> str:
        """
        Get ID of the subnetwork of specified network in specified availability zone

        :param parent_id: ID of the folder
        :param zone_id: ID of the availability zone
        :param network_id: ID of the network
        :return ID of the subnetwork
        """
        subnet_service = self.sdk.client(subnet_service_pb2, SubnetServiceStub)
        subnets = subnet_service.List(ListSubnetsRequest(parent_id=parent_id)).items
        if network_id:
            applicable = [s for s in subnets if s.spec.network_id == network_id]
        else:
            applicable = subnets
        if len(applicable) == 1:
            return applicable[0].metadata.id
        if len(applicable) == 0:
            raise RuntimeError(f"There are no subnets, please create it.")
        raise RuntimeError(f"There are more than one subnet, please specify it")
