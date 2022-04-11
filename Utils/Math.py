import numpy as np

#получение минора матрицы
def get_matrix_minor(m: list[list[float]], i: int, j: int) -> list[list[float]]:
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]


#нахождение определителя матрицы
def determinant(a: list[list[float]]) -> float:
    if len(a) == 1:
        pro = a[0][0]
        return pro

    elif len(a) == 2:
        pro = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return pro

    else:
        pro = 0
        for i in range(len(a[0])):
            pro += ((-1) ** i) * a[0][i] * determinant(get_matrix_minor(a, 0, i))
        return pro


def kramer_method(coefficients: list[list[float]], answers: list[float]):
    try:
        delta = determinant(coefficients)
        delta_arr = []
        for j in range(len(coefficients)):
            new_coefficients = coefficients[:][:j] + [answers] + coefficients[:][j+1:]
            delta_arr.append(determinant(new_coefficients))
        x_arr = []
        for i in range(len(delta_arr)):
            x_arr.append(delta_arr[i] / delta)
        return x_arr
    except ZeroDivisionError:
        return None
