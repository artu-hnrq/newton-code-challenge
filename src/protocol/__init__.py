import grpc
from concurrent import futures
from .calculate_pb2 import Calculation, Ready
from .calculate_pb2_grpc import TaskManagerServicer as Servicer, TaskManagerStub, add_TaskManagerServicer_to_server


class TaskManagerServicer(Servicer):
    def GetTask(self, request, context):
        task = Calculation()
        task.operation = Calculation.Operation.SUBTRACTION
        task.number[:] = [2, 3]
        return task


def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TaskManagerServicer_to_server(TaskManagerServicer(), server)
    server.add_insecure_port('[::]:50051')
    print('server listening port 50051')
    server.start()
    server.wait_for_termination()


def connect_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = TaskManagerStub(channel)
    response = stub.GetTask(Ready())
    print(response.operation)
    [print(n) for n in response.number]
