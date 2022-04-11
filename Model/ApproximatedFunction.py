from dataclasses import dataclass
from typing import Callable
import math
from Model.TableFunction import TableFunction


@dataclass
class ApproximatedFunction:
    f: Callable[[any], float]
    name: str
    deviation_measure: float
    standart_deviation: float
    approximation_reliability: float


def get_deviation_measure(table_function: TableFunction, f: Callable[[float], float]) -> float:
    s = 0
    for i in range(table_function.n):
        s += (f(table_function.x[i]) - table_function.y[i])**2
    return s


def get_standart_deviation(table_function: TableFunction, f: Callable[[float], float]):
    try:
        return math.sqrt(get_deviation_measure(table_function, f) / table_function.n)
    except ZeroDivisionError:
        return None


def get_approximation_reliability(table_function: TableFunction, f: Callable[[float], float]):
    try:
        sum_yfi = 0
        sum_fi2 = 0
        sum_fi = 0
        for i in range(table_function.n):
            sum_yfi += (table_function.y[i] - f(table_function.x[i]))**2
            sum_fi2 += f(table_function.x[i])**2
            sum_fi += f(table_function.x[i])
        return 1 - (sum_yfi / (sum_fi2 - ((sum_fi**2) / table_function.n)))
    except ZeroDivisionError:
        return None
