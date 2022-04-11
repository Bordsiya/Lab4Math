from Model.ApproximatedFunction import ApproximatedFunction, get_deviation_measure, get_standart_deviation, \
    get_approximation_reliability
from Model.TableFunction import TableFunction
from Utils.Math import kramer_method


def calculate_coefficients(table_function: TableFunction):
    sx = sum(table_function.x)
    sx2 = 0
    sx3 = 0
    sx4 = 0
    for i in range(table_function.n):
        sx2 += table_function.x[i]**2
        sx3 += table_function.x[i]**3
        sx4 += table_function.x[i]**4
    sy = sum(table_function.y)
    sxy = 0
    sx2y = 0
    for i in range(table_function.n):
        sxy += table_function.x[i] * table_function.y[i]
        sx2y += (table_function.x[i]**2) * table_function.y[i]
    matrix_coefficients = [[table_function.n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    answers = [sy, sxy, sx2y]
    return kramer_method(matrix_coefficients, answers)


def get_square_function(table_function: TableFunction):
    coefficients = calculate_coefficients(table_function)
    if coefficients is None:
        return None
    f = lambda x: coefficients[0] + coefficients[1] * x + coefficients[2] * (x**2)
    return ApproximatedFunction(
        f,
        "Аппроксимация полиномиальной функцией 2-ей степени",
        get_deviation_measure(table_function, f),
        get_standart_deviation(table_function, f),
        get_approximation_reliability(table_function, f)
    )

