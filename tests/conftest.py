import pytest


@pytest.fixture()
def token():
    return "AAAA00000000000000000000000000000000000"


@pytest.fixture()
def iam_token():
    return "xxxxxx"


@pytest.fixture()
def service_account_key():
    return {
        "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAtkLwDl1iX5z/1WGbkPCy\nz7016kLnkCsTnKcUpLs4cVzyVqjkZE2j4S+CTu7OhkB8AyVWCui9kjT2JH/uvllu\ntoZzVbiRptPcC3/m903pCemnfUlVF7AhU59PabCrzb24FLjuxyatYPE48I15gLOg\n+uSspJy4mYPZy8xX5KJ2rhWknfH5fH4V0JXWoIrVoK6mfoia2AFwz+jYzZCS2xiQ\nDyUhLX7yWI0wg77309GaBdqGhwuVKVd+XbGFoY5ltQI72NoRbBhkZB+nmEDZZtwk\nad0b+ydhetHCS5eS5pcC8T61SFQ7zSfr2dIawnpbmt3rfxwLVhwAi7n+Sy3bFbe6\nDUkirblzQRnKU+qh8BBrw88KNjqm2MvsTXj0qD1Wv7xLRXaNnpsmHqWkUVgjriia\nBKTePIw9rNmqBNoeLyrCP4lr+YFCvEy0BHqWZAw5StGCgoqng/Y5Hyljn6oRroCI\nxu77eqwQ6IegbLF7JSZMVsZR4D9yunvvjQXgbrJ9pm7hPn5VDl2FSyjZjl7lAj2v\noGVPKPsa4wVCPftc1c689onf1oeFVAX+34EBzD0rqttFPGh9KT/ugIqSqcE/AJ9d\n5XKd+yw+C2q4ycqMLhClBbJT7QvboHA6r5uZi17TpajGk6XDBmxW7eQXcvYKfJaA\nK8tfjlQxhvabjdcVrEO6DB0CAwEAAQ==\n-----END PUBLIC KEY-----\n",
        "sa_json": {
            "subject-credentials": {
                "type": "JWT",
                "alg": "RS256",
                "private-key": "-----BEGIN PRIVATE KEY-----\n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\noqublpCF+90//gckhlAfnrhT6mpsGQ==\n-----END PRIVATE KEY-----\n",
                "kid": "publickey-e00aaaaaaaaaaaaaaa",
                "iss": "serviceaccount-e00aaaaaaaaaaaaaaa",
                "sub": "serviceaccount-e00aaaaaaaaaaaaaaa",
            }
        },
    }
