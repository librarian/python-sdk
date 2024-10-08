import grpc
import os
import nebiusai
import logging
from nebius.compute.v1.instance_service_pb2_grpc import InstanceService, InstanceServiceStub
from nebius.iam.v1.tenant_user_account_service_pb2_grpc import TenantUserAccountServiceStub
from nebius.compute.v1.instance_service_pb2 import ListInstancesRequest
from nebius.iam.v1.tenant_user_account_service_pb2 import ListTenantUserAccountsRequest
import nebius.compute.v1.instance_service_pb2
import nebius.iam.v1.tenant_user_account_service_pb2

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)
parent_id = os.getenv("PARENT_ID")
token = os.env.getenv("IAM_TOKEN")
sdk = nebiusai.SDK(
        interceptor=nebiusai.RetryInterceptor(max_retry_count=5, retriable_codes=[grpc.StatusCode.UNAVAILABLE]),
        iam_token=token
)

instance_service = sdk.client(nebius.compute.v1.instance_service_pb2, InstanceServiceStub)
user_account_service = sdk.client(nebius.iam.v1.tenant_user_account_service_pb2, TenantUserAccountServiceStub)

print(instance_service.List(ListInstancesRequest(parent_id=parent_id)))
print(user_account_service.List(ListTenantUserAccountsRequest(parent_id=parent_id)))
