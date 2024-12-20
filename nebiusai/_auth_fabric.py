import logging
import os
import time
from datetime import datetime, timezone
from typing import Any, Dict, Optional, Union

# noinspection PyUnresolvedReferences
# jwt package depends on cryptography
import cryptography  # noqa: F401; pylint: disable=unused-import
import jwt
import requests
import six

from nebius.annotations_pb2 import api_service_name
from nebius.iam.v1.token_service_pb2 import ExchangeTokenRequest

_MDS_ADDR = "169.254.169.254"
_MDS_URL = "http://{}/computeMetadata/v1/instance/service-accounts/default/token"
_MDS_HEADERS = {"Metadata-Flavor": "Google"}
_MDS_TIMEOUT = (1.0, 1.0)  # 1sec connect, 1sec read

API_ENDPOINT = "api.eu.nebius.cloud"


def set_up_api_endpoint(endpoint: str) -> str:
    # pylint: disable-next=global-statement
    global API_ENDPOINT
    API_ENDPOINT = endpoint
    return API_ENDPOINT


def service_from_ctor(service_ctor: Any) -> str:
    if not hasattr(service_ctor, "DESCRIPTOR"):
        logging.debug("Service %s has no descriptor", service_ctor.__name__)
        return ""

    return service_ctor.DESCRIPTOR.package.split(".")[1]


def _get_api_service_url(service_ctor: Any) -> str:
    if not hasattr(service_ctor, "DESCRIPTOR"):
        logging.debug("Service %s has no descriptor", service_ctor.__name__)
        return API_ENDPOINT

    name = service_ctor.DESCRIPTOR.services_by_name.keys()[0]
    logging.debug("Service %s has descriptor", name)

    simple_prefix = service_ctor.DESCRIPTOR.package.split(".")[1]
    endpoint = simple_prefix + "." + API_ENDPOINT
    service_prefix = service_ctor.DESCRIPTOR.services_by_name[name].GetOptions().Extensions[api_service_name]
    if service_prefix:
        logging.debug("Service %s has prefix %s", name, service_prefix)
        endpoint = service_prefix + "." + API_ENDPOINT
    logging.debug("Service %s has endpoint %s", name, endpoint)
    return endpoint


def __validate_service_account_key(sa_key: Optional[dict]) -> bool:
    if not isinstance(sa_key, dict):
        raise RuntimeError(f"Invalid Service Account Key: expecting dictionary, actually got {type(sa_key)}")
    sa_key = sa_key.get("subject-credentials")
    obj_id = sa_key.get("kid")
    sa_id = sa_key.get("iss")
    private_key = sa_key.get("private-key")

    if not obj_id:
        raise RuntimeError("Invalid Service Account Key: missing key object id.")

    if not sa_id:
        raise RuntimeError("Invalid Service Account Key: missing service account id.")

    if not private_key:
        raise RuntimeError("Invalid Service Account Key: missing private key.")

    private_key_prefix = "-----BEGIN PRIVATE KEY-----"
    if not isinstance(private_key, six.string_types) or private_key_prefix not in private_key:
        error_message = (
            "Invalid Service Account Key: private key is in incorrect format."
            f"Should start with {private_key_prefix}.\n"
            "To obtain one you can use CLI: nebius iam auth-public-key generate --output sa.json --service-account-id <id>"
        )
        raise RuntimeError(error_message)
    return True


class MetadataAuth:
    def __init__(self, metadata_addr: str):
        self.__metadata_addr = metadata_addr

    def url(self) -> str:
        return _MDS_URL.format(self.__metadata_addr)

    def get_token(self) -> str:
        r = requests.get(self.url(), headers=_MDS_HEADERS, timeout=_MDS_TIMEOUT)
        r.raise_for_status()
        response = r.json()
        return response["access_token"]


class TokenAuth:
    def __init__(self, token: str):
        self.__oauth_token = token

    def get_token_request(self) -> "ExchangeTokenRequest":
        return ExchangeTokenRequest(oauth_token=self.__oauth_token)


class ServiceAccountAuth:
    __5_MINUTES_IN_SECONDS = 5.0 * 60.0

    def __init__(self, sa_key: Dict[str, str], endpoint: Optional[str] = None):
        self.__sa_key = sa_key["subject-credentials"]
        self._endpoint = endpoint if endpoint is not None else API_ENDPOINT

    def get_token_request(self) -> "ExchangeTokenRequest":
        return ExchangeTokenRequest(
            grant_type="urn:ietf:params:oauth:grant-type:token-exchange",
            requested_token_type="urn:ietf:params:oauth:token-type:access_token",
            subject_token=self.__prepare_request(self._endpoint),
            subject_token_type="urn:ietf:params:oauth:token-type:jwt",
        )

    def __prepare_request(self, endpoint: str) -> str:
        now = time.time()
        exp_utc = int(datetime.fromtimestamp(now + self.__5_MINUTES_IN_SECONDS, timezone.utc).timestamp())
        now_utc = int(datetime.fromtimestamp(now, timezone.utc).timestamp())
        payload = {
            "iss": self.__sa_key["iss"],
            "sub": self.__sa_key["sub"],
            "exp": exp_utc,
            "iat": now_utc,
        }

        headers = {
            "typ": self.__sa_key["type"],
            "alg": self.__sa_key["alg"],
            "kid": self.__sa_key["kid"],
        }
        logging.debug("Service Account Auth: %s", payload)
        logging.debug("Service Account Auth: %s", headers)

        return jwt.encode(payload, self.__sa_key["private-key"], algorithm=self.__sa_key["alg"], headers=headers)


class IamTokenAuth:
    def __init__(self, iam_token: str):
        self.__iam_token = iam_token

    def get_token(self) -> str:
        return self.__iam_token


def get_auth_token_requester(
    token: Optional[str] = None,
    service_account_key: Optional[dict] = None,
    iam_token: Optional[str] = None,
    metadata_addr: Optional[str] = None,
    endpoint: Optional[str] = None,
) -> Union["MetadataAuth", "TokenAuth", "IamTokenAuth", "ServiceAccountAuth"]:
    if endpoint is None:
        endpoint = API_ENDPOINT
    auth_methods = [("token", token), ("service_account_key", service_account_key), ("iam_token", iam_token)]
    auth_methods = [(auth_type, value) for auth_type, value in auth_methods if value is not None]

    if len(auth_methods) == 0:
        metadata_addr = metadata_addr if metadata_addr is not None else os.environ.get("METADATA_ADDR", _MDS_ADDR)
        return MetadataAuth(metadata_addr)

    if len(auth_methods) > 1:
        raise RuntimeError(f"Conflicting API credentials properties are set: {[auth[0] for auth in auth_methods]}.")

    if token is not None:
        return TokenAuth(token=token)
    if iam_token is not None:
        return IamTokenAuth(iam_token)
    if service_account_key is not None and __validate_service_account_key(service_account_key):
        return ServiceAccountAuth(service_account_key, endpoint)

    raise RuntimeError("Unknown auth method")
