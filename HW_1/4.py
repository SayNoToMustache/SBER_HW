'''
Задача 4.
Дана электрическая цепь, состоящая из 2-х последовательно соединенных проводников (сопротивление каждого известно).
Найти общее сопротивление цепи (округление результата необходимо выполнить до 1-го знака после запятой).

R = R1+R2
'''
from functions_for_hw import str_to_posible_float as spf

str = input('Введите R1: ')
R_1 = spf(str)
    
str = input('Введите R2: ')
R_2 = spf(str)
    
del str

print('R =', round(R_1 + R_2, 1))