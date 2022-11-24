'''Упражнение 6. 
Напишите функцию, которая принимает неограниченное количество числовых аргументов и возвращает кортеж из двух списков: 
отрицательных значений (отсортирован по убыванию); 
неотрицательных значений (отсортирован по возрастанию). 
'''


def negative_positive(*argv):
    negative = []
    positive = []
    for i in argv:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    negative.sort(reverse=True)
    positive.sort()
    return negative, positive


print(negative_positive(1, 2, 43, -1, -42, -7, 4, -5, 4))
