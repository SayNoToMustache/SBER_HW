'''
Задача 8. Сортировка трех чисел
Напишите программу, запрашивающую у пользователя три целых числа и выводящую их в упорядоченном виде – по возрастанию. 
Используйте функции min и max для нахождения наименьшего и наибольшего значений. 
Оставшееся число можно найти путем вычитания из суммы трех введенных чисел максимального и минимального.
'''

x_1 = int(input('Введите первое целое число: '))
x_2 = int(input('Введите второе целое число: '))
x_3 = int(input('Введите третье целое число: '))

min = min(x_1, x_2, x_3)
max = max(x_1, x_2, x_3)

print(f'{min}, {x_1 + x_2 + x_3 - min - max}, {max}')