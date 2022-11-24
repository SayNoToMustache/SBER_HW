'''Упражнение 9. 
Напишите программу, которая позволит пользователю преобразовывать числа из одной системы счисления в другую произвольным образом.
Ваша программа должна поддерживать все системы счисления в диапазоне от 2 до 16 как для входных, так и для выходных данных. 
Если пользователь выберет систему с основанием, выходящим за границы допустимого, на экран должна быть выведена ошибка. 
Разделите код программы на несколько функций, включая функцию, конвертирующую число из произвольной системы счисления в 
десятичную, и обратную функцию, переводящую значение из десятичной системы в произвольную. В основной программе необходимо 
запросить у пользователя исходную систему счисления, целевую систему, а также число для преобразования. 
''' 
 
def from_to(_from, _to, num:str): 
    letters = ['A', 'B', 'C', 'D', 'E', 'F'] 
    num = num.upper() 
    def s_this_num_is(num): 
        return int(num) if num.isdigit() else ord(num) - ord('A') + 10 
 
    def from_to_10(_from, num): 
        s = str(num) 
        s = s[::-1] 
        answ = 0 
        for i, _num in enumerate(s): 
            answ += s_this_num_is(_num) * _from**i 
        return answ 
 
    def this_num_is(num): 
        return str(num) if num < 10 else letters[num - 10] 
 
    def from10_to(_to, num): 
        answ = 0 
        s = '' 
        while True: 
            rediuse = num % _to 
            num //= _to 
            s += this_num_is(rediuse) 
            if num < _to: 
                s += this_num_is(num) 
                return s[::-1] 
     
    if _from == _to: 
        return num 
    it_is_10 = from_to_10(_from, num) 
    if _to != 10: 
        return from10_to(_to, it_is_10) 
    else: 
        return str(it_is_10) 
         
print(from_to(2, 10, '11011')) 
print(from_to(2, 16, '11011')) 
print(from_to(2, 14, '11011')) 
print(from_to(14, 10, '1D')) 
print(from_to(14, 2, '1D'))