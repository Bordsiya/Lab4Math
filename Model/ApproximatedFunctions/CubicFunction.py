
from Model.ApproximatedFunction import ApproximatedFunction, get_deviation_measure, get_standart_deviation, \
    get_approximation_reliability
from Model.TableFunction import TableFunction
from Utils.Math import kramer_method


def calculate_coefficients(table_function: TableFunction):
    sx = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sx5 = 0
    sx6 = 0
    for i in range(table_function.n):
        sx += table_function.x[i]
        sx2 += table_function.x[i]**2
        sx3 += table_function.x[i]**3
        sx4 += table_function.x[i]**4
        sx5 += table_function.x[i]**5
        sx6 += table_function.x[i]**6
    sy = 0
    sxy = 0
    sx2y = 0
    sx3y = 0
    for i in range(table_function.n):
        sy += table_function.y[i]
        sxy += table_function.x[i] * table_function.y[i]
        sx2y += (table_function.x[i]**2) * table_function.y[i]
        sx3y += (table_function.x[i]**3) * table_function.y[i]
    matrix_coefficients = [
        [table_function.n, sx, sx2, sx3],
        [sx, sx2, sx3, sx4],
        [sx2, sx3, sx4, sx5],
        [sx3, sx4, sx5, sx6]
    ]
    answers = [sy, sxy, sx2y, sx3y]
    return kramer_method(matrix_coefficients, answers)


def get_cubic_function(table_function: TableFunction):
    coefficients = calculate_coefficients(table_function)
    if coefficients is None:
        return None
    f = lambda x: coefficients[0] + coefficients[1] * x + coefficients[2] * (x**2) + coefficients[3] * (x**3)
    return ApproximatedFunction(
        f,
        "Аппроксимация полиномиальной функцией 3-ей степени",
        get_deviation_measure(table_function, f),
        get_standart_deviation(table_function, f),
        get_approximation_reliability(table_function, f)
    )
