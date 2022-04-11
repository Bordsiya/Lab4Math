from Model.ApproximatedFunction import ApproximatedFunction, get_deviation_measure, get_standart_deviation, \
    get_approximation_reliability
from Model.TableFunction import TableFunction
from Utils.Math import kramer_method
import math


def calculate_coefficients(table_function: TableFunction):
    sx = 0
    sxx = 0
    for i in range(table_function.n):
        sx += table_function.x[i]
        sxx += table_function.x[i]**2
    sy = 0
    sxy = 0
    for i in range(table_function.n):
        sy += table_function.y[i]
        sxy += table_function.x[i] * table_function.y[i]
    matrix_coefficients = [[sxx, sx], [sx, table_function.n]]
    answers = [sxy, sy]
    return kramer_method(matrix_coefficients, answers)


def get_linear_function(table_function: TableFunction):
    coefficients = calculate_coefficients(table_function)
    if coefficients is None:
        return None
    f = lambda x: coefficients[0]*x + coefficients[1]
    return ApproximatedFunction(
        f,
        "Линейная аппроксимация",
        get_deviation_measure(table_function, f),
        get_standart_deviation(table_function, f),
        get_approximation_reliability(table_function, f)
    )


def get_correlation_coefficient_pirson(table_function: TableFunction) -> float:
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    x_mean = sum(table_function.x) / table_function.n
    y_mean = sum(table_function.y) / table_function.n
    for i in range(table_function.n):
        sum_xy += (table_function.x[i] - x_mean) * (table_function.y[i] - y_mean)
        sum_x += (table_function.x[i] - x_mean)**2
        sum_y += (table_function.y[i] - y_mean)**2
    return sum_xy / (math.sqrt(sum_x * sum_y))
