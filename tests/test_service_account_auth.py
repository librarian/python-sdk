import time

import jwt
import pytest

from nebiusai._auth_fabric import get_auth_token_requester


def test_both_params_error(token, service_account_key):
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(
            token=token, service_account_key=service_account_key.get("sa_json")
        ).get_token_request()

    assert str(e.value) == "Conflicting API credentials properties are set: ['token', 'service_account_key']."


def test_invalid_service_account_type():
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=[]).get_token_request()

    assert str(e.value).startswith("Invalid Service Account Key: expecting dictionary, actually got")


@pytest.mark.parametrize(
    "key, error_msg",
    [
        ("kid", "Invalid Service Account Key: missing key object id."),
        ("iss", "Invalid Service Account Key: missing service account id."),
        ("private-key", "Invalid Service Account Key: missing private key."),
    ],
)
def test_service_account_no_id(service_account_key, key, error_msg):
    service_account_key.get("sa_json").get("subject-credentials").pop(key)

    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=service_account_key.get("sa_json")).get_token_request()

    assert str(e.value) == error_msg


def test_service_account_key(service_account_key):
    request_func = get_auth_token_requester(service_account_key=service_account_key.get("sa_json")).get_token_request
    request = request_func()

    now = int(time.time())
    headers = jwt.get_unverified_header(request.subject_token)
    parsed = jwt.decode(
        request.subject_token,
        key=service_account_key.get("public_key"),
        algorithms=["RS256"],
    )
    assert headers["typ"] == "JWT"
    assert headers["alg"] == "RS256"
    assert headers["kid"] == service_account_key.get("sa_json")["subject-credentials"]["kid"]

    assert parsed["iss"] == service_account_key.get("sa_json")["subject-credentials"]["iss"]
    assert now - 60 <= int(parsed["iat"]) <= now


def test_iam_token(iam_token):
    token_func = get_auth_token_requester(iam_token=iam_token).get_token
    token = token_func()
    assert token == iam_token
