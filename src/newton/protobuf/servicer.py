import logging
from uuid import uuid4
from .calculate_pb2 import Task, Response
from .calculate_pb2_grpc import TaskManagerServicer as Servicer

class TaskManagerServicer(Servicer):
    tasklist = []

    def __init__(self, id):
        self.id = id
        super(Servicer, self).__init__()

    def Request(self, calculation, context):
        self.tasklist.append(calculation)

        message = f"New calculation queued: {len(self.tasklist)} in total"
        logging.info(message)
        response = Response(message=message)

        return response

    def GetTask(self, client, context):
        logging.info(f"{client.name} requested a task")

        task = Task(server=self.id, id=uuid4().hex)
        if len(self.tasklist) > 0:
            task.work.append(self.tasklist.pop(0))

        return task
