from .server import get_connection
from .calculate_pb2 import Calculation, Client

def request_calculation(operation, args, port):
    conn = get_connection(port)

    operation = {
        'add': Calculation.Operation.ADDICTION,
        'sub': Calculation.Operation.SUBTRACTION,
        'mul': Calculation.Operation.MULTIPLICATION,
        'div': Calculation.Operation.DIVISION
    }[operation]

    response = conn.Request(
        Calculation(
            operation=operation,
            number=args
        )
    )

    return response.message


def get_task(name, port):
    conn = get_connection(port)

    task = conn.GetTask(
        Client(
            name=name
        )
    )
    return task.work
