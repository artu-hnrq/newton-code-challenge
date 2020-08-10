from operator import add, sub, mul, truediv
import logging
from . import sgbd


def execute(task):
    for calculation in task.work:
        func, result = calculate(calculation)
        logging.info(f"Calculation executed: {func} = {result}")

    sgbd.insert(task.server, task.id, func, result)


def calculate(calculation):
    result = calculation.number[0]

    operation, operator = {
        calculation.Operation.ADDICTION: (add, '+'),
        calculation.Operation.SUBTRACTION: (sub, '-'),
        calculation.Operation.MULTIPLICATION: (mul, '*'),
        calculation.Operation.DIVISION: (truediv, '/')
    }[calculation.operation]

    try:
        for n in calculation.number[1:]:
            result = operation(result, n)
    except ZeroDivisionError as e:
        result = f"ERROR: {e}"

    return (operator.join([str(n) for n in calculation.number]), result)
