'''Задача 8. 
N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание, 
где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это 
номер человека, который останется в кругу последним.
'''

N = int(input('Введите кол-во участников '))
K = int(input('Введите на каком k вылет '))


def next_step(this_list_: list, begin_num=0) -> int | list:
    """next step after county

    Args:
        this_list (list): what we count

    Returns:
        int|list: (who is next, [new_list without destroyed man])
    """
    this_list = this_list_.copy()
    print(f'Сейчас играют:\n{this_list}')
    out_man = (K + begin_num - 1) % len(this_list)
    print("Выбывает {}".format(this_list.pop(out_man)))
    print('\n')
    if out_man == len(this_list):  # это был последний
        return (0, this_list)
    else:
        return (out_man, this_list)


_list_ = [i for i in range(1, N+1)]

count_by = 0
while len(_list_) > 1:
    print(f'Счет идет с {_list_[count_by]}')
    count_by, _list_ = next_step(_list_, count_by)

print(f'Остался человек под номером {_list_[0]}')
