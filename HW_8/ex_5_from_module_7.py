'''Упражнение 5.
Необходимо реализовать калькулятор. Пользователь вводит строку из 3 элементов, разделенных пробелом - 
ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2
Операнды - целые числа. Операции - арифметические (включая деление нацело и нахождение остатка)
Напишите программу, которая обрабатывает введенную пользователем строку и  вычисляет полученное действие.
Пропишите обработку возможных ошибок. Программа не должна завершаться при первой же ошибке, она должна
предлагать пользователю исправить ошибку и попробовать посчитать результат заново.
'''


def calc(string: str):
    def calculate(op1, op2, op):
        if op == '+':
            return op1 + op2
        if op == '-':
            return op1 - op2
        if op == '*':
            return op1 * op2
        if op == '/':
            return op1 / op2
        if op == '//':
            return op1 // op2
        if op == '%':
            return op1 % op2
    i = 0
    while True:
        input_string = string
        input_string = input_string.split()
        try:
            o1, op, o2 = input_string
        except ValueError as e:
            print("Попробуй ввести ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2 еще раз, ты сможешь")
            i += 1
            return None
        try:
            o1 = int(o1)
            o2 = int(o2)
        except ValueError as e:
            print("Попробуй еще раз, первый и третий аргумент - чиселки")
            i += 1
            return None
        try:
            if op not in ['+', '-', '*', '/', '//', '%']:
                raise ValueError
        except ValueError as e:
            print(
                "Попробуй еще раз, второй аргумент что-то такое - ['+', '-', '*', '/', '//', '%']")
            i += 1
            return None

        try:
            answ = calculate(o1, o2, op)
        except ZeroDivisionError:
            print("Ну кто делит на ноль?")
            i += 1
            return None

        print(f"Вы справились, мои поздравления {o1} {op} {o2} = {answ}")
        return answ
        break

    if i >= 4:
        secret1 = 'd097d0b020'
        secret2 = 'd0bfd0bed0bfd18bd182d0bed0ba20d0bcd0bed0b6d0bdd0be20d0b1d18bd0bbd0be20d0b820d181d0b0d0bcd0bed0bcd18320d181d187d0b8d182d0b0d182d18c20d0bdd0b0d183d187d0b8d182d18cd181d18f21'
        print(bytes.fromhex(secret1).decode('utf-8'),
              i, bytes.fromhex(secret2).decode('utf-8'))
