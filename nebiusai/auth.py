from typing import Dict, Optional

import nebius.iam.v1.token_exchange_service_pb2
from nebius.iam.v1.token_exchange_service_pb2_grpc import TokenExchangeServiceStub
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
    client = sdk.client(nebius.iam.v1.token_exchange_service_pb2, TokenExchangeServiceStub)
    return client.Exchange(requester.get_token_request()).access_token
