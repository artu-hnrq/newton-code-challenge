import grpc
from concurrent import futures
from operator import add, sub, mul, truediv

from .calculate_pb2 import Calculation, Ready, Response
from .calculate_pb2_grpc import TaskManagerServicer as Servicer, TaskManagerStub, add_TaskManagerServicer_to_server

def calculate(calculation):
    result = calculation.number[0]
    operation = {
        calculation.Operation.ADDICTION: add,
        calculation.Operation.SUBTRACTION: sub,
        calculation.Operation.MULTIPLICATION: mul,
        calculation.Operation.DIVISION: truediv
    }[calculation.operation]

    for n in calculation.number[1:]:
        result = operation(result, n)

    return result

class TaskManagerServicer(Servicer):
    tasks = []

    def Request(self, calculation, context):
        self.tasks.append(calculation)
        response = Response()
        response.message = f"New calculation requested: {str(calculation)}"
        [print(task) for task in self.tasks]
        return response

    def GetTask(self, request, context):
        print(request)
        task = self.tasks.pop(0)
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


def request_calculation():
    channel = grpc.insecure_channel(f"localhost:{SERVER_PORT}")
    stub = TaskManagerStub(channel)

    response = stub.Request(
        Calculation(
            operation=0,
            number=[5,5]
        )
    )

    print(response)
