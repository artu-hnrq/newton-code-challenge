import grpc
from concurrent import futures
from operator import add, sub, mul, truediv
import logging

from .calculate_pb2 import Calculation, Task, Client, Response
from .calculate_pb2_grpc import TaskManagerServicer as Servicer, TaskManagerStub, add_TaskManagerServicer_to_server

logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')

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
    tasklist = []

    def Request(self, calculation, context):
        self.tasklist.append(calculation)

        message = "New calculation queued:\n{}".format(str(calculation))
        logging.info(message)
        response = Response(message=message)

        return response

    def GetTask(self, client, context):
        logging.info(f"{client.name} requested a task")

        task = Task()
        if len(self.tasklist) > 0:
            task.work.append(self.tasklist.pop(0))

        return task



def start_server(port=5000):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TaskManagerServicer_to_server(TaskManagerServicer(), server)

    server.add_insecure_port(f"[::]:{port}")
    print(f"server listening port {port}")

    server.start()
    server.wait_for_termination()


def estabilish_connection(port=5000):
    channel = grpc.insecure_channel(f"localhost:{port}")
    return TaskManagerStub(channel)


def connect_client(name, port=5000):
    stub = estabilish_connection(port)

    task = stub.GetTask(Client(name=name))
    if task.work:
        for work in task.work:
            logging.info(f"The result is {calculate(work)}")
    else:
        logging.info("There's no more work to be done. Go get some rest!")



def request_calculation(operation, args, port=5000):
    stub = estabilish_connection(port)

    operation = {
        'add': Calculation.Operation.ADDICTION,
        'sub': Calculation.Operation.SUBTRACTION,
        'mul': Calculation.Operation.MULTIPLICATION,
        'div': Calculation.Operation.DIVISION
    }[operation]

    response = stub.Request(
        Calculation(
            operation=operation,
            number=args
        )
    )

    logging.info(response.message)
