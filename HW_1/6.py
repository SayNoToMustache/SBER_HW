'''
Задача 6. Поездка по кругу
Спортсмен решил потренироваться перед марафоном и покататься вокруг города на скорость. Длина дороги — 123 километра. 
Спортсмен стартует с нулевого километра и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
Реализуйте программу, которая спрашивает у пользователя v и t и выводит целое число от 0 до 122 — номер километра, 
на котором остановится Спортсмен. Учтите, что он может прокатиться больше одного круга.
'''
# Из условия задачи следует, что числа v и t целые? Решу для этого варианта, тк иначе не понятно какой километр писать в ответ

str = input('v = ')
v = int(str)
str = input('t = ')
t = int(str)

del str

print(f'Спортсмен со скоростью {v}км/ч и за время {t}ч остановится на {v*t % 123} километре')