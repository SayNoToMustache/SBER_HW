'''
Задача 7. Сумма и произведение цифр в числе
Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.
'''
sum = 0
pr = 1
str = input('Введите двузначное число: ')
for char in str:
    sum += int(char)
    pr *= int(char)
print(f'{str}: \n  sum = {sum},\n  mul = {pr};')

sum = 0
pr = 1
str = input('Введите трехзначное число: ')
for char in str:
    sum += int(char)
    pr *= int(char)
print(f'{str}: \n  sum = {sum},\n  mul = {pr};')


'''
Во время выполнения этого задания до меня дошло, что возможно требовалось знание деления поэтому покажу на трехзначном числе

str = input('Введите трехзначное число: ')
num = int(str)
sum = num // 100 + (num // 10) % 10 + num % 10
pr = (num // 100) * ((num // 10) % 10) * (num % 10)
print(f'{str}: \n  sum = {sum},\n  mul = {pr};')

'''