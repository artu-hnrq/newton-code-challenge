import grpc
from concurrent import futures

from .servicer import TaskManagerServicer
from .calculate_pb2_grpc import add_TaskManagerServicer_to_server, TaskManagerStub


def start(port=5000):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TaskManagerServicer_to_server(TaskManagerServicer(), server)

    server.add_insecure_port(f"[::]:{port}")
    print(f"server listening port {port}")

    server.start()
    server.wait_for_termination()


def get_connection(port=5000):
    channel = grpc.insecure_channel(f"localhost:{port}")
    return TaskManagerStub(channel)
