import logging
from .calculate_pb2 import Task, Response
from .calculate_pb2_grpc import TaskManagerServicer as Servicer

logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')

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
