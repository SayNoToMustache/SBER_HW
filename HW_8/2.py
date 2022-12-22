'''Упражнение 2.
Как вы знаете, в языке Python для создания комментариев в коде используется символ #. 
Комментарий начинается с этого символа и продолжается до конца строки – без возможности остановить его раньше. 
В данном упражнении вам предстоит написать программу, которая будет удалять все комментарии из исходного файла 
с кодом на языке Python. Пройдите по всем строкам в файле на предмет поиска символа #. Обнаружив его, 
программа должна удалить все содержимое, начиная с этого символа и до конца строки. 
Для простоты не будем рассматривать ситуации, когда знак решетки встречается в середине строки. 
Сохраните новое содержимое в созданном файле. 
Имена файла источника и файла назначения должны быть запрошены у пользователя. 
Удостоверьтесь в том, что программа корректно обрабатывает возможные ошибки при работе с обоими файлами.
'''

# file1 = input("Введите файл который нужно преобразовать")
# file2 = input("Введите файл куда нужно отправить")
# with open("HW_8/file1", 'r', encoding="utf-8") as fd1, open("HW_8/file2", "w", encoding='utf-8') as fd2:
    
with open("HW_8/2_file_to_delete.txt", 'r', encoding="utf-8") as fd1, open("HW_8/2_file_with_delete.txt", "w", encoding='utf-8') as fd2:
    for s in fd1:
        for j in s:
            if j == '#':
                fd2.write('\n')
                break
            fd2.write(j)