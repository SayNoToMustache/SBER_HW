'''
Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со словами
... - чемпион!

После этого выполните:
используя операцию дублирования, нарисуйте черту (набор "-"), длиной, равной размеру названия команды;
преобразуйте строку в нижний регистр и выведите на экран:
длину наименования команды;
есть ли в наименовании команды буква "п" (True/False)?
сколько раз повторяется буква "а"?
'''

_str = input()
print(f'{_str} - чемпион!')

# TODO тут скобки не нужны для символа строки
ex_1 = len(_str) * '-'
print(ex_1)

_str = _str.lower()
print(_str)

# TODO и тут тоже не нужны
if 'п' in _str:
    print('True')
else:
    print('False')
    
print(_str.count('а'))
