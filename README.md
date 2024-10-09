[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![License][license-image]][license-url]

<!-- Badges -->

[build-image]: https://github.com/librarian/python-sdk/actions/workflows/run-tests.yml/badge.svg
[build-url]: https://github.com/librarian/python-sdk/actions/workflows/run-tests.yml
[license-image]: https://img.shields.io/github/license/librarian/python-sdk.svg
[license-url]: https://github.com/librarian/python-sdk/blob/master/LICENSE

# Nebius SDK (Python)

Need to automate your infrastructure or use services provided by Nebius? We've got you covered.

Installation:

    pip install nebiusai

## Getting started

There are several options for authorization your requests - OAuth Token,
Metadata Service (if you're executing your code inside VMs or Cloud Functions
running in Nebius), Service Account Keys, and externally created IAM tokens.

### OAuth Token

```python
sdk = nebiusai.SDK(token='AQAD-.....')
```

### Metadata Service

Don't forget to assign Service Account for your Instance or Function and grant required roles.

```python
sdk = nebiusai.SDK()
```

### Service Account Keys

```python
# you can store and read it from JSON file
sa_key = {
    "id": "...",
    "service_account_id": "...",
    "private_key": "..."
}

sdk = nebiusai.SDK(service_account_key=sa_key)
```

### IAM tokens

```python
sdk = nebiusai.SDK(iam_token="t1.9eu...")
```

Check `examples` directory for more examples.

### Override service endpoint

#### Supported services

| Service Name                                                           | Alias                    |
|------------------------------------------------------------------------|--------------------------|

| nebius.cloud.compute                                                   | compute                  |
| nebius.cloud.registry                                                  | container-registry       |
| nebius.cloud.iam                                                       | iam                      |
| nebius.cloud.storage                                                   | storage-api              |
| nebius.cloud.vpc                                                       | vpc                      |


#### Override in client
```python
import nebius.vpc.v1.network_service_pb2 as network_service
from nebius.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from nebiusai import SDK

sdk = SDK(iam_token="t1.9eu...")
new_network_client_endpoint = "example.new.vpc.very.new:50051"
insecure = False # by default is False, but if server does not support verification can be set to True
network_client = sdk.client(network_service NetworkServiceStub, endpoint=new_network_client_endpoint, insecure=False)
```

#### Override in sdk config
To override endpoints provide dict in format {alias : new-endpoint}
```python
import nebius.vpc.v1.network_service_pb2 as network_service
from nebius.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from nebiusai import SDK
new_network_client_endpoint = "example.new.vpc.very.new:50051"
sdk = SDK(iam_token="t1.9eu...", endpoints={"vpc": new_network_client_endpoint})
insecure = False # by default is False, but if server does not support verification can be set to True
network_client = sdk.client(network_service, NetworkServiceStub, insecure=False)
```

Notice: if both overrides are used for same endpoint, override by client has priority


## Contributing
### Dependencies
Use `make deps` command to install library, its production and development dependencies.

### Formatting
Use `make format` to autoformat code with black tool.

### Tests
- `make test` to run tests for current python version
- `make lint` to run only linters for current python version
- `make tox-current` to run all checks (tests + code style checks + linters + format check) for current python version
- `make tox` to run all checks for all supported (installed in your system) python versions
- `make test-all-versions` to run all checks for all supported python versions in docker container


### Maintaining
If pull request consists of several meaningful commits, that should be preserved,
then use "Rebase and merge" option. Otherwise use "Squash and merge".

New release (changelog, tag and pypi upload) will be automatically created
on each push to master via Github Actions workflow.
