from Model.ApproximatedFunctions.CubicFunction import get_cubic_function
from Model.ApproximatedFunctions.ExponentialFunction import get_exponential_function
from Model.ApproximatedFunctions.LinearFunction import get_linear_function
from Model.ApproximatedFunctions.LogarithmicFunction import get_log_function
from Model.ApproximatedFunctions.PowerFunction import get_power_function
from Model.ApproximatedFunctions.SquareFunction import get_square_function
from Utils.GraphMethods import draw_graph
from Utils.IOMethods import read_table_function, print_results

table_function = read_table_function()

approximations = []

cubic_approximation = get_cubic_function(table_function)
if cubic_approximation is not None:
    approximations.append(cubic_approximation)
exponential_approximation = get_exponential_function(table_function)
if exponential_approximation is not None:
    approximations.append(exponential_approximation)
linear_approximation = get_linear_function(table_function)
if linear_approximation is not None:
    approximations.append(linear_approximation)
logarithmic_approximation = get_log_function(table_function)
if logarithmic_approximation is not None:
    approximations.append(logarithmic_approximation)
power_approximation = get_power_function(table_function)
if power_approximation is not None:
    approximations.append(power_approximation)
square_approximation = get_square_function(table_function)
if square_approximation is not None:
    approximations.append(square_approximation)

mn_standart_deviation_func = approximations[0]
for i in range(len(approximations)):
    if approximations[i].standart_deviation < mn_standart_deviation_func.standart_deviation:
        mn_standart_deviation_func = approximations[i]

if mn_standart_deviation_func.name == "Аппроксимация полиномиальной функцией 3-ей степени":
    print_results(table_function, cubic_approximation)
    draw_graph(table_function, cubic_approximation)
elif mn_standart_deviation_func.name == "Экспоненциальная аппроксимация":
    print_results(table_function, exponential_approximation)
    draw_graph(table_function, exponential_approximation)
elif mn_standart_deviation_func.name == "Линейная аппроксимация":
    print_results(table_function, linear_approximation)
    draw_graph(table_function, linear_approximation)
elif mn_standart_deviation_func.name == "Логарифмическая аппроксимация":
    print_results(table_function, logarithmic_approximation)
    draw_graph(table_function, logarithmic_approximation)
elif mn_standart_deviation_func.name == "Степенная аппроксимация":
    print_results(table_function, power_approximation)
    draw_graph(table_function, power_approximation)
else:
    print_results(table_function, square_approximation)
    draw_graph(table_function, square_approximation)
