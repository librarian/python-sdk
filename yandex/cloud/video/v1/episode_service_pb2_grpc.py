# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import episode_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_episode__pb2
from yandex.cloud.video.v1 import episode_service_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2


class EpisodeServiceStub(object):
    """Episode management service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/Get',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__pb2.Episode.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/List',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/Create',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.CreateEpisodeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/Update',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.UpdateEpisodeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/Delete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.DeleteEpisodeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.PerformAction = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/PerformAction',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.PerformEpisodeActionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetPlayerURL = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/GetPlayerURL',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLResponse.FromString,
                )
        self.GetManifests = channel.unary_unary(
                '/yandex.cloud.video.v1.EpisodeService/GetManifests',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsResponse.FromString,
                )


class EpisodeServiceServicer(object):
    """Episode management service.
    """

    def Get(self, request, context):
        """Returns the specific channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List episodes for stream or line.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create episode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update episode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete episode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformAction(self, request, context):
        """Perform an action on the episode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayerURL(self, request, context):
        """Returns url to the player.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManifests(self, request, context):
        """Returns manifest urls.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EpisodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__pb2.Episode.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.CreateEpisodeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.UpdateEpisodeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.DeleteEpisodeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'PerformAction': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformAction,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.PerformEpisodeActionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetPlayerURL': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerURL,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLResponse.SerializeToString,
            ),
            'GetManifests': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManifests,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.video.v1.EpisodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EpisodeService(object):
    """Episode management service.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/Get',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__pb2.Episode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/List',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.ListEpisodesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/Create',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.CreateEpisodeRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/Update',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.UpdateEpisodeRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/Delete',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.DeleteEpisodeRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/PerformAction',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.PerformEpisodeActionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayerURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/GetPlayerURL',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodePlayerURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManifests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.EpisodeService/GetManifests',
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_episode__service__pb2.GetEpisodeManifestsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
