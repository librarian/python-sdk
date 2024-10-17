import time
from concurrent import futures

import grpc

import nebius.compute.v1.image_pb2 as image_pb2
import nebius.compute.v1.image_service_pb2 as image_service_pb2
import nebius.compute.v1.image_service_pb2_grpc as image_service_pb2_grpc

_DEFAULT_SERVICE_PORT = "50051"
_SERVICE_ADDR = "localhost:" + _DEFAULT_SERVICE_PORT

DEFAULT_IMAGE = image_pb2.Image()


class ImageServiceMock(object):
    def __init__(self, handler):
        self.__handler = handler

    def Get(self, request, context):
        return self.__handler(context)

    def GetByName(self, request, context):
        return self.__handler(context)

    def GetLatestByFamily(self, request, context):
        return self.__handler(context)

    def List(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        return image_service_pb2.ListImagesResponse()

    def ListOperationsByParent(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        return image_service_pb2.ListOperationsResponse()


def grpc_server(handler):
    service = ImageServiceMock(handler)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:" + _DEFAULT_SERVICE_PORT)
    image_service_pb2_grpc.add_ImageServiceServicer_to_server(service, server)
    server.start()
    assert _is_grpc_endpoint_ready(60)
    return server


def default_channel():
    return grpc.insecure_channel(_SERVICE_ADDR)


def _is_grpc_endpoint_ready(timeout):
    def check_endpoint_ready():
        channel = grpc.insecure_channel(_SERVICE_ADDR)
        client = image_service_pb2_grpc.ImageServiceStub(channel)

        try:
            client.List(image_service_pb2.ListImagesRequest(), timeout=1)
        except grpc.RpcError as e:
            return e.code() not in [grpc.StatusCode.UNAVAILABLE, grpc.StatusCode.DEADLINE_EXCEEDED]

        return True

    deadline = time.time() + timeout

    while time.time() <= deadline:
        if check_endpoint_ready():
            return True

    return False
