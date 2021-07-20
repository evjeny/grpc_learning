from concurrent import futures
import logging

import grpc

from interfaces import capitalizer_pb2_grpc
from server.server import Capitalizer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    capitalizer_pb2_grpc.add_CapitalizerServicer_to_server(Capitalizer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()