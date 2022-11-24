'''Упражнение 5. 
Используя шифр Цезаря (достаточно только букв русского алфавита, знаки препинания не изменяются) зашифруйте, а затем расшифруйте введенную строку. 
'''


def cesarus(s: str, shift=5, is_ban_list=True) -> str:
    s_list = list(s)
    ban_list = []
    if is_ban_list:
        ban_list = [' ', ',', '.', '!', '?']
    for i, char in enumerate(s_list):
        if char in ban_list:
            continue
        else:
            index = ord(char) - ord('а')
            index += shift
            index %= 32
            index += ord('а')
            s_list[i] = chr(index)
    return ''.join(s_list)


def decipher_cesarus(s: str, shift=5, is_ban_list=True) -> str:
    s_list = list(s)
    ban_list = []
    if is_ban_list:
        ban_list = [' ', ',', '.', '!', '?']
    for i, char in enumerate(s_list):
        if char in ban_list:
            continue
        else:
            index = ord(char) - ord('а')
            index -= shift
            index %= 32
            index += ord('а')
            s_list[i] = chr(index)
    return ''.join(s_list)


s = 'лол, что происходит?'
cipher = cesarus(s)
print(cipher)
print(decipher_cesarus(cipher))
