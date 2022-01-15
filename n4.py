''' Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''
in_numb=int(input('Введите целое положительное число - '))

max_numb=0
while in_numb >0:
    tempo = in_numb%10
    max_numb=tempo if tempo > max_numb else max_numb
    in_numb = in_numb//10
print(f'Максимальная цифра во введенном числе равна {max_numb}')
