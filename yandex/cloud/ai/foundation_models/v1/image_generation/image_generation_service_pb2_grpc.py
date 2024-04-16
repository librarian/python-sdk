# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.ai.foundation_models.v1.image_generation import image_generation_service_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ImageGenerationAsyncServiceStub(object):
    """Service for obtaining images from input data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService/Generate',
                request_serializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ImageGenerationAsyncServiceServicer(object):
    """Service for obtaining images from input data.
    """

    def Generate(self, request, context):
        """A method for generating an image based on a textual description.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageGenerationAsyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageGenerationAsyncService(object):
    """Service for obtaining images from input data.
    """

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService/Generate',
            yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
