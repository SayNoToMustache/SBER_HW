'''
Задача 5.
Дано уравнение ax + b = 0 и отрезок [m;n]. Ответьте на вопрос, попадает ли решение уравнения в указанный отрезок.
'''
from functions_for_hw import str_to_posible_float as spf

str = input('Введите а: ')
a = spf(str)
print('a = ', a)    

str = input('Введите b: ')
b = spf(str)

str = input('Введите m: ')
m = spf(str)

str = input('Введите n: ')
n = spf(str)
    
del str

print(f'Задано уравнение:')
print(f'{a}x + {b} = 0')

def f(x):
    return a*x + b

right = f(m)
left = f(n)

if (right * left <= 0):
    print('True')
else:
    print('False')


