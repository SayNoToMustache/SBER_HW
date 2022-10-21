"""
Задача 1

В задаче «Подсчитать отрицательные числа в отсортированной матрице» нам
дается матрица из n строк и m столбцов. Элементы сортируются в порядке
убывания как по строкам, так и по столбцам. Нам нужно найти общее
количество отрицательных элементов в матрице.

In: grid = [[8,3,2,-1],[4,2,1,-1],[3,1,-1,-2],[-1,-1,-2,-3]]
Out: 8
"""

"""
 8  3  2 -1
 4  2  1 -1
 3  1 -1 -2
-1 -1 -2 -3
"""


def find_negative_value(matrix: list) -> int:
    """Подсчет количества отрицательных элементов в матрице

    Args:
        matrix (список N x M): матрица представленна в виде списка
    """
    j = len(matrix) - 1  # hight
    i = len(matrix[0]) - 1  # wight
    _count = 0

    if matrix[j][i] >= 0:
        return 0

    for j_num in range(j, -1, -1):
        for i_num in range(i, -1, -1):
            if matrix[j_num][i_num] >= 0:
                break
            _count += 1
    return _count


def sort_by_every(matrix: list) -> list:
    """сортирует массив по каждой строке и столбцу

    Args:
        matrix (list): матрица которую сортируем

    Returns:
        матрица: отсортированная матрица
    """
    _len_matrix = len(matrix)
    _height_matrix = len(matrix[0])

    # Распаковка
    _temp_list = []
    for _elem in matrix:
        _temp_list += _elem

    # Сортировка и раскидывание элементов
    _temp_list.sort(reverse=True)
    answ = [[]]

    for i in range(_len_matrix):
        for j in range(_height_matrix):
            answ[i].append(_temp_list[i * _height_matrix + j])
        answ.append([])
    del answ[_len_matrix]

    return answ


def pp_matrix(matrix: list):
    """красивый вывод матрицы на экран

    Args:
        matrix (list): выводимая матрица
    """
    print(5 * len(matrix[0]) * ("-"))
    for i in matrix:
        for u in i:
            print("{:4d}".format(u), end=" ")
        print("")
    print(5 * len(matrix[0]) * ("-"))


grid = [[8, 3, 2, -1], [4, 2, 1, -1], [3, 1, -1, -2], [-1, -1, -2, -3]]
pp_matrix(grid)
grid = sort_by_every(grid)
pp_matrix(grid)
print(find_negative_value(grid))
