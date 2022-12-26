'''Упражнение 1.
На вход подается файл input_numbers.txt, где записано N целых чисел, которые могут 
быть разделены пробелами и концами строк. Напишите программу, которая выводит 
сумму чисел в выходной файл output_sum.txt
'''

answ = 0
with open("HW_8/input_numbers.txt", 'r', encoding="utf-8") as file, \
        open("HW_8/output_sum.txt", 'w', encoding="utf-8") as out:
    for i in file:
        s = i.strip()
        s = s.split()
        answ += sum(int(j) for j in s)
    out.write(str(answ))
