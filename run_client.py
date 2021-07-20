from __future__ import print_function
import logging

import io
from PIL import Image

import grpc

from interfaces import capitalizer_pb2, capitalizer_pb2_grpc


def print_call(stub_method, message: str, description: str):
    result = stub_method(capitalizer_pb2.StringRequest(message=message))
    print(description, result.message)


def example_image_request(stub_method):
    temp_image = Image.new("RGB", (200, 200), "white")
    buffer = io.BytesIO()
    temp_image.save(buffer, "png")

    response = stub_method(capitalizer_pb2.FileRequest(file=buffer.getvalue()))
    buffer = io.BytesIO(response.file)
    result_image = Image.open(buffer)
    result_image.show()


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = capitalizer_pb2_grpc.CapitalizerStub(channel)

        print_call(stub.Capitalize, "hello", "Capitalize:")
        print_call(stub.Upper, "HeLlO", "Upper:")
        print_call(stub.Lower, "HeLlO", "Lower:")
        example_image_request(stub.DrawA)


if __name__ == '__main__':
    logging.basicConfig()
    run()