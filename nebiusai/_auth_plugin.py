from datetime import datetime
from typing import TYPE_CHECKING, Callable, Optional, Tuple, Union
import logging
import grpc
from six.moves.urllib.parse import urlparse

from nebius.iam.v1.token_exchange_service_pb2_grpc import TokenExchangeServiceStub

if TYPE_CHECKING:
    from nebius.iam.v1.token_service_pb2 import CreateIamTokenResponse
    from nebiusai._auth_fabric import (
        IamTokenAuth,
        MetadataAuth,
        ServiceAccountAuth,
        TokenAuth,
    )


TIMEOUT_SECONDS = 20


class Credentials(grpc.AuthMetadataPlugin):
    def __init__(
        self,
        token_requester: Union["MetadataAuth", "TokenAuth", "IamTokenAuth", "ServiceAccountAuth"],
        lazy_channel: Callable[[], "grpc.Channel"],
    ):
        # pylint: disable=super-init-not-called
        self.__token_requester = token_requester
        self._lazy_channel = lazy_channel
        self._channel: Optional[grpc.Channel] = None
        self._cached_access_token: str = ""
        self._access_token_timestamp: Optional[datetime] = None

    def __call__(self, context: "grpc.AuthMetadataContext", callback: "grpc.AuthMetadataPluginCallback") -> None:
        try:
            return self._call(context, callback)
        except Exception as exception:  # pylint: disable=broad-except
            callback(tuple(), exception)
        return None

    def _call(self, context: "grpc.AuthMetadataContext", callback: "grpc.AuthMetadataPluginCallback") -> None:
        u = urlparse(context.service_url)
        logging.info("Service URL: %s", u)
        if u.path in (
            "/nebius.iam.v1.TokenExchangeService",
        ):
            logging.info("Skipping auth for IAM service")
            callback(tuple(), None)
            return

        if self._channel is None:
            self._channel = self._lazy_channel()

        if not self._fresh():
            get_token = getattr(self.__token_requester, "get_token", None)
            logging.info("Getting token: %s", get_token)
            if callable(get_token):
                logging.info("Getting token (callable get_token): %s", get_token)
                self._cached_access_token = get_token()
                self._access_token_timestamp = datetime.now()
                callback(self._metadata(), None)
                return

            get_token_request = getattr(self.__token_requester, "get_token_request", None)
            if callable(get_token_request):
                logging.info("Getting token request (callable get_token_request): %s", get_token_request)
                token_future = TokenExchangeServiceStub(self._channel).Exchange.future(get_token_request())
                token_future.add_done_callback(self.create_done_callback(callback))
                return

        callback(self._metadata(), None)

    def create_done_callback(self, callback: "grpc.AuthMetadataPluginCallback") -> Callable[["grpc.Future"], None]:
        def done_callback(future: "grpc.Future") -> None:
            try:
                resp = future.result()
            except Exception as exception:  # pylint: disable=broad-except
                callback(tuple(), exception)
            else:
                self._save_token(resp)
                callback(self._metadata(), None)

        return done_callback

    def _metadata(self) -> Tuple[Tuple[str, str]]:
        metadata = (("authorization", f"Bearer {self._cached_access_token}"),)
        return metadata

    def _save_token(self, resp: "CreateTokenResponse") -> None:
        self._cached_access_token = resp.access_token
        self._access_token_timestamp = datetime.now()

    def _fresh(self) -> bool:
        if self._cached_access_token == "":
            return False
        if self._access_token_timestamp is None:
            return False
        diff = datetime.now() - self._access_token_timestamp
        return diff.total_seconds() < TIMEOUT_SECONDS
