
# Возвращает int от строки, если число в строке целое, если оно разделено ., то переводит его в float
# Например '11111' -> 11111
# Например '1111.1111' -> 1111.1111
def str_to_posible_float(str):
    if (str.find('.') == -1):
        A = int(str)
    else:
        str = str.split('.')
        print(str)
        A = int(str[0])
        if (A >= 0):
            A += int(str[1]) / (10 ** len(str[1]))
        else:
            A -= int(str[1]) / (10 ** len(str[1]))
    return A