from operator import add, sub, mul, truediv
import logging
from . import sgbd

def execute(task):
    for calculation in task.work:
        result = calculate(calculation)
        logging.info(f"Calculation executed: {result}")

    sgbd.insert(task.id, str(task.work[0]), result)


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

def create_db():
    conn = sqlite3.connect('newton.db')
    conn.execute(
        '''
        CREATE TABLE TASK (
            ID INT PRIMARY KEY NOT NULL,
            FUNC CHAR(50)    NOT NULL,
            RESULT CHAR(50) NOT NULL
        );
        '''
    )
    conn.close()
