import matplotlib.pyplot as plt
import numpy as np

from Model.ApproximatedFunction import ApproximatedFunction
from Model.TableFunction import TableFunction


def get_linspace_equation(table_function: TableFunction):
    mn = min(table_function.x) - 0.5
    mx = max(table_function.x) + 0.5
    return np.linspace(mn, mx, 200)


def draw_graph(table_function: TableFunction, approximated_function: ApproximatedFunction):
    plt.gcf().canvas.set_window_title("График функции")
    plt.grid()
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    X = get_linspace_equation(table_function)
    F = approximated_function.f
    F = np.vectorize(F)
    plt.xticks(np.arange(min(X), max(X) + 1, 1.0))
    axes.plot(X, F(X))

    axes.scatter(table_function.x, table_function.y, c='red')

    plt.savefig('graph')
