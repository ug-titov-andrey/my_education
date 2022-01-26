'''Создать программный файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.'''
import sys
file_name='user_data1.txt'
try:
    f = open(file_name, 'w')
    while True:
        inp_str = input('Введите любую строку. Для выхода введите пустую строку => ')
        if inp_str == '':
            break
        f.writelines(inp_str + '\n')
except IOError:
    print('Ошибка записи в файл.')
finally:
    f.close()

