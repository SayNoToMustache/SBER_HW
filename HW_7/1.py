'''
58-61 - может не быть имени в accounts, 66 - отрицательное или строка
'''


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

    При переводе денежных средств необходимо учитывать:
        - хватает ли денег на счету, с которого осуществляется перевод;
        - перевод состоит из уменьшения баланса первого счета и увеличения
            баланса второго; если хотя бы на одном этапе происходит ошибка,
            аккаунты должны быть приведены в первоначальное состояние
            (механизм транзакции)
            см. https://ru.wikipedia.org/wiki/Транзакция_(информатика).

    Исключения (raise):
        - NoMoneyToWithdrawError: на счету 'account_from'
                                    не хватает денег для перевода;
        - PaymentError: ошибка при переводе.
    """
    if account_from not in accounts.keys():
        raise Exception("PaymentError")
    if account_to not in accounts.keys():
        raise Exception("PaymentError")
    try:
        if value < 0:
            raise Exception("PaymentError")
    except ValueError as er:
        raise Exception("PaymentError")
    if accounts[account_from] < value:
        raise Exception("NoMoneyToWithdrawError")
    accounts[account_from] -= value
    accounts[account_to] += value


if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".
          format(**payment_info))

    payment_info["value"] = int(input("Сумма = "))

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)
