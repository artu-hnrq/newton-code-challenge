import unittest, random
from newton.protobuf import Calculation, Task, Client, Response, TaskManagerServicer


def create_Calculation():
    return Calculation(
        operation=random.choice(Calculation.Operation.keys()),
        number=[random.randint(0, 99) for i in range(5)]
    )


def create_Servicer():
    return TaskManagerServicer(random.randint(0, 99))


class Test_Protobuf_Messages(unittest.TestCase):
    "Simple protobuf objects field presence / type test"

    def test_Calculation(self):
        create_Calculation()

    def test_Task(self):
        Task(
            server=1,
            id="id1"
        )
        Task(
            server=2,
            id="id2",
            work=[
                create_Calculation()
                for i in range(2)
            ]
        )

    def test_Client(self):
        Client()
        Client(name='name')

    def test_Response(self):
        Response()
        Response(message='message')


class Test_Protobuf_Servicer(unittest.TestCase):
    "Protobuf servicer class methods test"

    def test_Request(self):
        servicer = create_Servicer()

        response = servicer.Request(create_Calculation(), None)
        self.assertIsInstance(response, Response)
        self.assertEquals(len(servicer.tasklist), 1)

    def test_GetTask(self):
        servicer = create_Servicer()

        task = servicer.GetTask(Client(name='name'), None)
        self.assertIsInstance(task, Task)
        self.assertEquals(task.server, servicer.id)
        self.assertFalse(task.work)
