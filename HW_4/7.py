'''Упражнение 7.  
Строка называется палиндромом, если она пишется одинаково в обоих направлениях. Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah». Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом. 
'''


def is_pal(s: str) -> bool:
    s = s.lower()
    j = len(s) - 1
    for i in range(len(s)//2):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


s = 'level'
print('is pal \'{}\' ? {}'.format(s, is_pal(s)))
s = 'levil'
print('is pal \'{}\' ? {}'.format(s, is_pal(s)))
s = ''
print('is pal \'{}\' ? {}'.format(s, is_pal(s)))
