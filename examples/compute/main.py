#!/usr/bin/env python3
import argparse
import json
import logging
import os

import grpc

import nebiusai
import nebius.compute.v1.image_service_pb2 as image_service_pb2
import nebius.compute.v1.instance_service_pb2 as instance_service_pb2
import nebius.compute.v1.disk_service_pb2 as disk_service_pb2
from nebius.compute.v1.image_service_pb2 import GetImageLatestByFamilyRequest
from nebius.compute.v1.image_service_pb2_grpc import ImageServiceStub
from nebius.compute.v1.instance_pb2 import Instance, AttachedDiskSpec,ResourcesSpec, ExistingDisk

from nebius.compute.v1.instance_service_pb2 import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
)
from nebius.common.v1.metadata_pb2 import ResourceMetadata
from nebius.compute.v1.disk_service_pb2 import CreateDiskRequest
from nebius.compute.v1.disk_pb2 import DiskSpec, Disk
from nebius.compute.v1.disk_service_pb2_grpc import DiskServiceStub
from nebius.compute.v1.instance_service_pb2_grpc import InstanceServiceStub
from nebius.compute.v1.network_interface_pb2 import NetworkInterfaceSpec, PublicIPAddress

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)
TIMEOUT = 60

def create_disk(sdk: nebiusai.SDK, parent_id, source_image_id):
    logging.info("Creating disk")
    request = CreateDiskRequest(
        metadata=ResourceMetadata(
            parent_id=parent_id,
            name="disk"
        ),
        spec=DiskSpec(
            type=DiskSpec.DiskType.NETWORK_SSD_NON_REPLICATED,
            size_gibibytes=93,
            source_image_id=source_image_id
        )
    )
    result = sdk.create_operation_and_get_result(
        request=request,
        service=DiskServiceStub,
        service_ctor=disk_service_pb2,
        meta_type=ResourceMetadata,
        method_name="Create",
        response_type=Disk,
        logger=logger,
        timeout=TIMEOUT
    )
    logging.info("Disk created: %s", result.response.id)

    return result.response.id

def create_instance(sdk, parent_id,  name, subnet_id):
    logging.info("Creating instance")

    image_service = sdk.client(image_service_pb2, ImageServiceStub)
    source_image_id = image_service.GetLatestByFamily(
        GetImageLatestByFamilyRequest(parent_id="project-e00public-images", image_family="ubuntu22.04-driverless")
    )
    logging.info("source_image_id: %s", source_image_id.metadata.id)
    disk_id = create_disk(sdk, parent_id, source_image_id.metadata.id)
    subnet_id = subnet_id or sdk.helpers.get_subnet(parent_id)
    request = CreateInstanceRequest(
        metadata=ResourceMetadata(
            parent_id=parent_id,
            name=name,
        ),
        resources_spec=ResourcesSpec(
            platform="cpu-e2",
            preset="80vcpu-320gb"

        ),
        boot_disk=AttachedDiskSpec(
            attach_mode=AttachedDiskSpec.AttachMode.ATTACH_MODE_READ_WRITE,
            existing_disk=ExistingDisk(id=disk_id),
            device_id="boot"
        ),
        network_interface_specs=[
            NetworkInterfaceSpec(
                subnet_id=subnet_id,
                public_ip_address=PublicIPAddress(static=False)
            ),
        ],

    )
    result = sdk.create_operation_and_get_result(
        request=request,
        service=InstanceServiceStub,
        service_ctor=instance_service_pb2,
        method_name="Create",
        response_type=Instance,
        meta_type=ResourceMetadata,
        logger=logger,
        timeout=TIMEOUT
    )

    logging.info("Creating initiated")
    return result.response.id


def delete_instance(sdk: nebiusai.SDK, instance_id):
    request = DeleteInstanceRequest(id=instance_id)
    return sdk.create_operation_and_get_result(
        request=request,
        service=InstanceServiceStub,
        service_ctor=instance_service_pb2,
        method_name="Delete",
        logger=logger,
        timeout=TIMEOUT
    )

def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    interceptor = nebiusai.RetryInterceptor(max_retry_count=5, retriable_codes=[grpc.StatusCode.UNAVAILABLE])
    if arguments.token:
        sdk = nebiusai.SDK(interceptor=interceptor, token=arguments.token)
    elif arguments.metadata_addr:
        sdk = nebiusai.SDK(interceptor=interceptor, metadata_addr=arguments.metadata_addr)
    elif arguments.iam_token:
        sdk = nebiusai.SDK(interceptor=interceptor, iam_token=os.getenv(arguments.iam_token,))
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = nebiusai.SDK(interceptor=interceptor, service_account_key=json.load(infile))

    fill_missing_arguments(sdk, arguments)

    instance_id = None
    try:
        instance_id = create_instance(sdk, arguments.parent_id, arguments.name, arguments.subnet_id)

    finally:
        if instance_id:
            logging.info("Deleting instance {}".format(instance_id))
            print(delete_instance(sdk, instance_id))



def fill_missing_arguments(sdk, arguments):
    if not arguments.subnet_id:
        network_id = sdk.helpers.find_network_id(parent_id=arguments.parent_id)
        arguments.subnet_id = sdk.helpers.find_subnet_id(
            parent_id=arguments.parent_id,
            network_id=network_id,
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    auth = parser.add_mutually_exclusive_group(required=True)
    auth.add_argument(
        "--sa-json-path",
        help="Path to the service account key JSON file.\nThis file can be created using YC CLI:\n"
        "yc iam key create --output sa.json --service-account-id <id>",
    )
    auth.add_argument("--token", help="OAuth token")
    auth.add_argument("--metadata-addr", help="Metadata address")
    auth.add_argument("--iam-token", help="IAM token")
    parser.add_argument("--parent-id", help="Your parent id", required=True)
    parser.add_argument("--name", default="demo-instance", help="New instance name.")
    parser.add_argument("--subnet-id", help="Subnet of the instance")

    return parser.parse_args()


if __name__ == "__main__":
    main()
