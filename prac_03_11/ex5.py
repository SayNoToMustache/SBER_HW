'''Упражнение 5. Простое число?
Простое число представляет собой число, большее единицы, которое без остатка делится
лишь на само себя и единицу. Напишите функцию для определения того, является ли введенное
число простым. Возвращаемое значение должно быть либо True, либо False. В основной программе, как
и ожидается, пользователь должен ввести целое число и получить ответ о том, является ли оно простым.
Убедитесь, что основная программа не будет запускаться, если файл импортирован в другой файл в качестве модуля.
'''

# Делать цикл от 2 до корня из числа это не интересно, зря я что-ли учился
from random import randint


def is_it_prime(num: int) -> bool:
    """is num prime or not?

    Args:
        num (int): num to factor

    Returns:
        bool: True if prime
    """

    # num = 2**s * d + 1, where s and d are positive integers and d is odd
    # let 0 < a < num is base
    # and k accuracy
    # then complexity of algorithm = O(k * log(n)**3)

    if num % 2 == 0 or num == 1:
        return False
    num_1 = num - 1
    s = 0
    while num_1 % 2 == 0:
        s += 1
        num_1 //= 2
    d = num_1

    print(f'{num} = 2**{s} * {d} + 1')

    k = 1000
    for i in range(k):
        a = randint(2, num - 2)
        x = a**d % num
        if x == 1 or x == num-1:
            continue  # while True
        for i in range(s-1):
            x = x**2 % num
            if x == num - 1:
                break  # while True
        if x == num - 1:
            continue
        return False
    return True


print(is_it_prime(97))
