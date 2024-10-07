from typing import Dict, Optional

from nebius.iam.v1.token_service_pb2_grpc import IamTokenServiceStub
from nebiusai._auth_fabric import (
    API_ENDPOINT,
    IamTokenAuth,
    MetadataAuth,
    get_auth_token_requester,
)
from nebiusai._sdk import SDK


def get_auth_token(
    token: Optional[str] = None,
    service_account_key: Optional[Dict[str, str]] = None,
    iam_token: Optional[str] = None,
    metadata_addr: Optional[str] = None,
    endpoint: Optional[str] = None,
) -> str:
    if endpoint is None:
        endpoint = API_ENDPOINT
    requester = get_auth_token_requester(
        token=token,
        service_account_key=service_account_key,
        iam_token=iam_token,
        metadata_addr=metadata_addr,
        endpoint=endpoint,
    )
    if isinstance(requester, (MetadataAuth, IamTokenAuth)):
        return requester.get_token()

    sdk = SDK()
    client = sdk.client(IamTokenServiceStub)
    return client.Create(requester.get_token_request()).iam_token
