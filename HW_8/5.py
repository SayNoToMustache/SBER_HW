'''Упражнение 5.
В папке с домашними заданиями лежит архив voina-i-mir.zip. Напишите программу, которая подсчитывает статистику
по символам в этом романе и выведет результат в файл. Результат должен быть отсортирован по частоте
встречаемости букв (по возрастанию). Регистр символов имеет значение.
Реализуйте программу так, чтобы для её работы не требовалась распаковка архива “в ручную” -
https://docs.python.org/3/library/zipfile.html
'''

import zipfile

freq_d = {}

if zipfile.is_zipfile("HW_8/voyna-i-mir.zip"):
    with zipfile.ZipFile("HW_8/voyna-i-mir.zip", mode="r") as zf:
        # print(zf.namelist()) # Нашли что лежит
        for i in zf.open('voyna-i-mir.txt', "r"):
            for sym in bytes(i).decode('utf-8'):
                if sym in freq_d.keys():
                    freq_d[sym] += 1
                else:
                    freq_d[sym] = 1

print(freq_d)
