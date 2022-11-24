'''Упражнение 8. 
Вы загадываете число от 1 до 100 (включительно). Компьютер спрашивает у вас «Твое число равно, меньше или больше, чем число N?»,  где N — число, которое хочет проверить компьютер. 
Вы отвечаете одним из трёх чисел: 
1 — равно, 
2 — больше, 
3 — меньше. 
 
Напишите программу, которая с помощью цепочки таких вопросов и ответов угадывает число. 
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток. 
'''


def num_game():
    n = 50
    residue = 50
    i = 1
    text = 'attempt[{}]: your number is {}?\n enter: 1-eq, 2-g, 3-l\n'
    while True:
        answ = int(input((text.format(i, n))))
        residue //= 2
        residue = (max(residue, 1))
        if answ == 1:
            print('PC win')
            return n
        if answ == 2:
            n += residue
        elif answ == 3:
            n -= residue
        else:
            print('let\'s start again, u can\'t understand these simple rules?')
            return num_game()
        i += 1


num_game()
