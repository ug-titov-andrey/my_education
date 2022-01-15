'''Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

inp_numb=input('введите любое натуральное число - ')
out_numb= int(inp_numb) + int(inp_numb*2) + int(inp_numb*3)
print(f'сумма  {inp_numb} + {inp_numb*2} + {inp_numb*3} равна {out_numb}')