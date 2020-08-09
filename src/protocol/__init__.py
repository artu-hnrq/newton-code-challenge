import grpc
from concurrent import futures
from .calculate_pb2 import Calculation, Ready
from .calculate_pb2_grpc import TaskManagerServicer as Servicer, TaskManagerStub, add_TaskManagerServicer_to_server

def calculate(calculation):
    result = calculation.number[0]

    for n in calculation.number[1:]:
        if calculation.operation == calculation.Operation.ADDICTION:
            result += n
        if calculation.operation == calculation.Operation.SUBTRACTION:
            result -= n
        if calculation.operation == calculation.Operation.MULTIPLICATION:
            result *= n
        if calculation.operation == calculation.Operation.DIVISION:
            result /= n

    return result


class TaskManagerServicer(Servicer):
    def GetTask(self, request, context):
        print(request)
        task = Calculation()
        task.operation = Calculation.Operation.MULTIPLICATION
        task.number[:] = [2, 3, 4]
        return task


SERVER_PORT = 5000

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TaskManagerServicer_to_server(TaskManagerServicer(), server)

    server.add_insecure_port(f"[::]:{SERVER_PORT}")
    print(f"server listening port {SERVER_PORT}")

    server.start()
    server.wait_for_termination()


def connect_client():
    channel = grpc.insecure_channel(f"localhost:{SERVER_PORT}")
    stub = TaskManagerStub(channel)

    response = stub.GetTask(Ready(client_id=0))

    print(calculate(response))
