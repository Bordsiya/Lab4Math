from Model.ApproximatedFunction import ApproximatedFunction
from Model.ApproximatedFunctions.LinearFunction import get_correlation_coefficient_pirson
from Model.TableFunction import TableFunction
from Utils.Exceptions import exceptions_arr
from tabulate import tabulate


def read_table_function() -> TableFunction:
    read_line = input

    def close_file():
        return None

    table_function = TableFunction(0, [], [])

    #Определение источника ввода исходных данных
    inp = input('Вы желаете ввести исходные данные из файла? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        try:
            file = open(file_name, 'r')
            read_line = lambda x: file.readline()
            close_file = file.close
        except FileNotFoundError or IOError:
            print('Ошибка: ', exceptions_arr['FileNotFound'])
            exit(1)
    elif inp not in ['N', 'n']:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)

    points_amount = int(read_line('Введите количество заданных точек: '))
    if points_amount <= 0:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)

    #if points_amount < 10:
        #print('Ошибка: ', exceptions_arr['TooLittleArguments'], '- Должно быть передано минимум 10 точек')
        #close_file()
        #exit(1)
    #if points_amount > 12:
        #print('Ошибка: ', exceptions_arr['TooManyArguments'], '- Должно быть передано максимум 12 точек')
        #close_file()
        #exit(1)
    table_function.n = points_amount

    #Ввод точек
    try:
        print('Введите координаты точек построчно: ')
        for i in range(points_amount):
            point_str = read_line('').strip()
            point_arr = list(point_str.split())

            if len(point_arr) > 2:
                print('Ошибка: ', exceptions_arr['TooMuchArguments'])
                close_file()
                exit(1)

            x = float(point_arr[0].replace(',', '.'))
            y = float(point_arr[1].replace(',', '.'))
            table_function.x.append(x)
            table_function.y.append(y)

    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)
    except IndexError:
        print('Ошибка: ', exceptions_arr['TooLittleArguments'])
        close_file()
        exit(1)

    close_file()
    return table_function


def print_results(table_function: TableFunction, approximated_function: ApproximatedFunction):
    print_data = print

    def close_file():
        return None

    inp = input('Вы желаете вывести результаты в файл? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        try:
            file = open(file_name, 'w+')
            print_data = lambda x: print(x, file=file)
            close_file = file.close
        except FileNotFoundError or IOError:
            print('Ошибка: ', exceptions_arr['FileNotFound'])
            exit(1)
    elif inp not in ['N', 'n']:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)

    approximated_y = []
    for i in range(table_function.n):
        approximated_y.append(approximated_function.f(table_function.x[i]))

    table = []
    for i in range(table_function.n):
        table.append([table_function.x[i], table_function.y[i], approximated_y[i]])
    headers = ["x", "y", "fi(x)"]

    print_data(approximated_function.name)
    print_data('\n')
    print_data(tabulate(table, headers, tablefmt="github"))
    print_data('\n')
    print_data("Мера отклонения: ")
    print_data(approximated_function.deviation_measure)
    print_data('\n')
    print_data("Среднеквадратическое отклонение: ")
    print_data(approximated_function.standart_deviation)
    print_data('\n')
    print_data("Достоверность аппроксимации: ")
    print_data(approximated_function.approximation_reliability)
    print_data('\n')

    if approximated_function.name == "Линейная аппроксимация":
        print_data("Коэффициент корреляции: ")
        print_data(get_correlation_coefficient_pirson(table_function))
        print_data('\n')
    close_file()


