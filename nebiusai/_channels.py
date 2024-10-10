import logging
from importlib.metadata import PackageNotFoundError, version
from typing import Dict, Optional

import grpc

from nebiusai import _auth_plugin
from nebiusai._auth_fabric import API_ENDPOINT, get_auth_token_requester, _get_api_service_url
import nebius.iam.v1.token_exchange_service_pb2 as token_exchange_service_pb2

try:
    VERSION = version("nebiusai")
except PackageNotFoundError:
    VERSION = "0.0.0"

SDK_USER_AGENT = f"nebius-python-sdk/{VERSION}"
logger = logging.getLogger(__name__)


class Channels:
    def __init__(
        self,
        client_user_agent: Optional[str] = None,
        endpoints: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        iam_token: Optional[str] = None,
        endpoint: Optional[str] = None,
        service_account_key: Optional[Dict[str, str]] = None,
        root_certificates: Optional[bytes] = None,
        private_key: Optional[bytes] = None,
        certificate_chain: Optional[bytes] = None,
        **_: str,
    ) -> None:
        self._channel_creds = grpc.ssl_channel_credentials(
            root_certificates=root_certificates,
            private_key=private_key,
            certificate_chain=certificate_chain,
        )
        self._endpoint = endpoint if endpoint is not None else API_ENDPOINT
        self._token_requester = get_auth_token_requester(
            token=token,
            service_account_key=service_account_key,
            iam_token=iam_token,
            endpoint=self._endpoint,
        )

        self._client_user_agent = client_user_agent
        self._config_endpoints = endpoints if endpoints is not None else {}
        self._endpoints: Optional[Dict[str, str]] = None
        self.channel_options = tuple(
            ("grpc.primary_user_agent", user_agent)
            for user_agent in [self._client_user_agent, SDK_USER_AGENT]
            if user_agent is not None
        )

    def channel(self, service: str, endpoint: Optional[str] = None, insecure: bool = False) -> grpc.Channel:
        if endpoint:
            logger.info("Using provided service %s endpoint %s", service, endpoint)
            if insecure:
                logger.debug("Insecure option is ON, no IAM endpoint used for verification")
                return grpc.insecure_channel(endpoint, options=self.channel_options)
            iam_endpoint = _get_api_service_url(token_exchange_service_pb2)
            logger.debug("Insecure option is OFF,IAM endpoint %s used for verification", iam_endpoint)
            creds: grpc.ChannelCredentials = self._get_creds(iam_endpoint)
            return grpc.secure_channel(endpoint, creds, options=self.channel_options)
        if service not in self._config_endpoints and insecure:
            logger.warning(
                "Unable to use insecure option for default {%s} service endpoint.\n"
                "Option is ignored. To enable it override endpoint.",
                service,
            )
        elif insecure:
            logger.debug("Insecure option is ON, no IAM endpoint used for verification")
            return grpc.insecure_channel(self.endpoints[service], options=self.channel_options)

        logger.info(
            "Using endpoints from configuration, IAM %s, %s %s",
            self.endpoints["iam"],
            service,
            self.endpoints[service],
        )

        iam_endpoint = _get_api_service_url(token_exchange_service_pb2)
        creds = self._get_creds(iam_endpoint)
        if service not in self.endpoints:
            raise RuntimeError(f"Unknown service: {service}")
        return grpc.secure_channel(self.endpoints[service], creds, options=self.channel_options)

    @property
    def endpoints(self) -> Dict[str, str]:
        if self._endpoints is None:
            self._endpoints = {}
            self._endpoints["iam"] = API_ENDPOINT
            self._endpoints["compute"] = "compute." + API_ENDPOINT
            self._endpoints["registry"] = "registry." + API_ENDPOINT
            self._endpoints["mk8s"] = "mk8s." + API_ENDPOINT
            for id_, address in self._config_endpoints.items():
                logger.debug("Override service %s, endpoint %s", id_, address)
                if id_ == "iam":
                    logger.warning(
                        "Be aware `iam` service endpoint is overridden. "
                        "That can produce unexpected results in SDK calls."
                    )
                self._endpoints[id_] = address
        return self._endpoints


    def _get_creds(self, iam_endpoint: str) -> grpc.ChannelCredentials:
        plugin = _auth_plugin.Credentials(
            self._token_requester, lambda: grpc.secure_channel(iam_endpoint, creds, options=self.channel_options)
        )
        call_creds = grpc.metadata_call_credentials(plugin)
        creds = grpc.composite_channel_credentials(self._channel_creds, call_creds)
        return creds
