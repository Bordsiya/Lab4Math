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
            sx += table_function.x[i]
            sxx += table_function.x[i]**2
        sy = 0
        sxy = 0
        for i in range(table_function.n):
            sy += math.log(table_function.y[i], math.e)
            sxy += table_function.x[i] * math.log(table_function.y[i], math.e)
        matrix_coefficients = [[sxx, sx], [sx, table_function.n]]
        answers = [sxy, sy]
        coefficients = kramer_method(matrix_coefficients, answers)
        coefficients[1] = math.e**(coefficients[1])
        coefficients[0], coefficients[1] = coefficients[1], coefficients[0]
        return coefficients
    except ValueError:
        return None


def get_exponential_function(table_function: TableFunction):
    coefficients = calculate_coefficients(table_function)
    if coefficients is None:
        return None
    f = lambda x: coefficients[0] * (math.e**(coefficients[1]*x))
    return ApproximatedFunction(
        f,
        "Экспоненциальная аппроксимация",
        get_deviation_measure(table_function, f),
        get_standart_deviation(table_function, f),
        get_approximation_reliability(table_function, f)
    )
