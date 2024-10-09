#!/usr/bin/env python3
import argparse
import json
import logging
import os

import grpc

import nebiusai
import nebius.compute.v1.image_service_pb2 as image_service_pb2
import nebius.compute.v1.instance_service_pb2 as instance_service_pb2
from nebius.compute.v1.image_service_pb2 import GetImageLatestByFamilyRequest
from nebius.compute.v1.image_service_pb2_grpc import ImageServiceStub
from nebius.compute.v1.instance_pb2 import Instance, AttachedDiskSpec,ResourcesSpec

from nebius.compute.v1.instance_service_pb2 import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
)
from nebius.common.v1.metadata_pb2 import ResourceMetadata
from nebius.compute.v1.instance_service_pb2_grpc import InstanceServiceStub
from nebius.compute.v1.network_interface_pb2 import NetworkInterfaceSpec, PublicIPAddress


def create_instance(sdk, parent_id,  name, subnet_id):
    image_service = sdk.client(image_service_pb2, ImageServiceStub)
    source_image = image_service.GetLatestByFamily(
        GetImageLatestByFamilyRequest(parent_id="standard-images", image_family="ubuntu-2204")
    )
    subnet_id = subnet_id or sdk.helpers.get_subnet(parent_id)
    instance_service = sdk.client(instance_service_pb2, InstanceServiceStub)
    operation = instance_service.Create(
        CreateInstanceRequest(
            parent_id=parent_id,
            name=name,
            resources_spec=ResourcesSpec(
                memory=2 * 2**30,
                cores=2,
                core_fraction=0,
            ),
            platform_id="standard-v1",
            boot_disk_spec=AttachedDiskSpec(
                auto_delete=True,
                disk_spec=AttachedDiskSpec.DiskSpec(
                    type_id="network-hdd",
                    size=20 * 2**30,
                    image_id=source_image.id,
                ),
            ),
            network_interface_specs=[
                NetworkInterfaceSpec(
                    subnet_id=subnet_id,
                    public_ip_address=PublicIPAddress(static=False)

                ),
            ],
            metadata={
                "metadata-key": "metadata-value",
            },
        )
    )
    logging.info("Creating initiated")
    return operation


def delete_instance(sdk, instance_id):
    instance_service = sdk.client(instance_service_pb2, InstanceServiceStub)
    return instance_service.Delete(DeleteInstanceRequest(instance_id=instance_id))


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
        operation = create_instance(sdk, arguments.parent_id, arguments.name, arguments.subnet_id)
        operation_result = sdk.wait_operation_and_get_result(
            instance_service_pb2,
            operation,
            response_type=Instance,
            meta_type=ResourceMetadata,
        )

        instance_id = operation_result.response.id

    finally:
        if instance_id:
            logging.info("Deleting instance {}".format(instance_id))
            operation = delete_instance(sdk, instance_id)
            sdk.wait_operation_and_get_result(
                instance_service_pb2,
                operation,
                meta_type=ResourceMetadata,
            )


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
