'''Упражнение 1.
Списки в языке Python могут содержать в себе вложенные списки. В тоже время вложенные списки могут также 
состоять из списков, тем самым увеличивая глубину общей иерархии. В результате списки могут обретать структуру, 
похожую на следующую: [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]].
Списки со множеством уровней вложенности могут пригодиться при описании сложных отношений между элементами, 
но при этом такая структура значительно усложняет выполнение операций над элементами.
Процесс выравнивания (flattening) списка заключается в избавлении от вложенной структуры и простом перечислении 
входящих в него элементов. Допустим, для приведенного выше примера выровненный список будет выглядеть так: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
'''


class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def flattening(this_list_arg: list) -> list:
    """list flattening

    Args:
        this_list_arg (list): [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]

    Returns:
        list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    if not isinstance(this_list_arg, list):
        if not isinstance(this_list_arg, tuple):
            print(f'{bcolors.FAIL}Enter List or Tuple!{bcolors.ENDC}')
            # exit()
            return None
    this_list = this_list_arg.copy()
    if len(this_list) < 1:
        return []
    if isinstance(this_list[0], int):
        return [this_list[0]] + flattening(this_list[1:])
    if isinstance(this_list[0], list):
        return flattening(this_list[0]) + flattening(this_list[1:])


print(flattening([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
print(flattening([]))
print(flattening(1))
