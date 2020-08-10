import logging
from operator import add, sub, mul, truediv

def execute(calculations):
    for calculation in calculations:
        logging.info(f"Calculation executed: {calculate(calculation)}")


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
