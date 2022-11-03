"""Задача 7. 
Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики любого размера, 
которые не меньше размера его ноги. 
Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей. 
Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься. 
"""

sk_size_s = input("Введите размеры коньков через пробел:\n")
sk_size = [int(x) for x in sk_size_s.split()]
hmn_size_s = input("Введите размеры ног людей через пробел:\n")
hmn_size_s.split()
hmn_size = [int(x) for x in hmn_size_s.split()]

del sk_size_s
del hmn_size_s

hmn_size.sort(reverse=True)
sk_size.sort()

# Получается сортированный список чел разм [42, 32, 31, 30]
# и список размеров роликов [30, 31, 41, 45]
print(hmn_size)
human_can = 0
for i in hmn_size:
    if any(i <= sk_size_buf for sk_size_buf in sk_size):
        for j, sk_size_buf in enumerate(sk_size):
            if i <= sk_size_buf:
                human_can += 1
                sk_size.pop(j)
                break
if human_can >= 2 and human_can < 5:
    print(f'{human_can} человека, которые одновременно смогут кататься')
else:
    print(f'{human_can} человек, которые одновременно смогут кататься')
