from Model.ApproximatedFunction import ApproximatedFunction, get_deviation_measure, get_standart_deviation, \
    get_approximation_reliability
from Model.TableFunction import TableFunction
from Utils.Math import kramer_method
import math


def calculate_coefficients(table_function: TableFunction):
    try:
        sx = 0
        sxx = 0
        for i in range(table_function.n):
            sx += math.log(table_function.x[i], math.e)
            sxx += math.log(table_function.x[i], math.e)**2
        sy = 0
        sxy = 0
        for i in range(table_function.n):
            sy += table_function.y[i]
            sxy += math.log(table_function.x[i], math.e) * table_function.y[i]
        matrix_coefficients = [[sxx, sx], [sx, table_function.n]]
        answers = [sxy, sy]
        coefficients = kramer_method(matrix_coefficients, answers)
        return coefficients
    except ValueError:
        return None


def get_log_function(table_function: TableFunction):
    coefficients = calculate_coefficients(table_function)
    if coefficients is None:
        return None
    f = lambda x: coefficients[0] * math.log(x, math.e) + coefficients[1]
    return ApproximatedFunction(
        f,
        "Логарифмическая аппроксимация",
        get_deviation_measure(table_function, f),
        get_standart_deviation(table_function, f),
        get_approximation_reliability(table_function, f)
    )
