'''
Задача 2. Калькулятор
Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
арифметические: +, -, * , / , // , %, **, log10;
сравнение: <, <=, >, >=, !=, ==,
выводя на экран результат каждого действия. В случае получение вещественного результата, округлите его до 2-х знаков после запятой (используя функцию round()).
Подсказка. Функцию log10 вы найдете в модуле math.
'''

from math import log10

str = input('Введите 2 числа: ')
if (str.find(' ') != -1):
    str = str.split(' ')
    var_1, var_2 = str
    var_1 = int(var_1)//1
    var_2 = int(var_2)//1
else:
    var_1 = int(str)//1
    str = input('Введите второе число: ')
    var_2 = int(str)//1
    
print(f'{var_1} + {var_2} =', round(var_1 + var_2, 2))
print(f'{var_1} - {var_2} =', round(var_1 - var_2, 2))
print(f'{var_1} * {var_2} =', round(var_1 * var_2, 2))
print(f'{var_1} / {var_2} =', round(var_1 / var_2, 2))
print(f'{var_1} // {var_2} =', round(var_1 // var_2, 2))
print(f'{var_1} % {var_2} =', round(var_1 % var_2, 2))
print(f'{var_1} ** {var_2} =', round(var_1 ** var_2, 2))
print(f'log10 {var_1} =', round(log10(var_1), 2))
print(f'log10 {var_2} =', round(log10(var_2), 2))

print(f'{var_1} > {var_2} ?', var_1 > var_2)
print(f'{var_1} < {var_2} ?', var_1 < var_2)
print(f'{var_1} >= {var_2} ?', var_1 >= var_2)
print(f'{var_1} <= {var_2} ?', var_1 <= var_2)
print(f'{var_1} != {var_2} ?', var_1 != var_2)
print(f'{var_1} == {var_2} ?', var_1 == var_2)