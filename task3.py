'''В main запустить функцию run с параметром от 1 до 6.
Будет запущена соответсвующая номеру задания функция
Все необходимые входные параметры задаются в соответствующей ветке run'''


''' Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.'''
from sympy.abc import alpha


def n1(x1, x2):
    try:
        return x1/x2
    except ZeroDivisionError:
        print('В нашей математике на на ноль не делят. Попробуйте еще раз')
        raise ZeroDivisionError







'''2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, 
год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.'''

def n2(**kwarg):
    out_str=''
    for param in kwarg.items():
        out_str+="%s => %s,\t"%(param[0], param[1])
    return(out_str)

'''Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.'''
def n3(x1,x2,x3):
    if x1 >= x2:
        a=x1
        if x2 >= x3:
            b=x2
        else:
            b=x3
    else:
        a=x2
        if x1 >= x3:
            b=x1
        else:
            b=x3
    return(a+b)
''' Программа принимает действительное положительное число 
x и целое отрицательное число y. Необходимо выполнить возведение 
числа x в степень y. Задание необходимо реализовать в виде функции 
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
 с помощью оператора **. Второй — более сложная реализация без оператора **, 
 предусматривающая использование цикла.'''
def n4(Foundation, Degree):
    foundation = float(Foundation)
    degree = int(Degree)
    classic_rez= foundation**degree
    my_rez = 1
    for value in range(abs(degree)):
        my_rez *=foundation if degree>=0 else 1/foundation
    return classic_rez, my_rez


'''Программа запрашивает у пользователя строку чисел, 
разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова 
нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее
 сумме и после этого завершить программу'''

def n5():
    sum_out = 0
    while True:
        sum_tempo=0
        flag_out = False
        numb_str = input('Введите разделенных пробелом. Для выходя введите q - ').split(' ')
        for value in numb_str:
            if value =='q':
                flag_out = True
                break
            else:
                try:
                    sum_tempo += float(value)
                except ValueError:
                    print(f'{value} не является числом и будет пропущено')
        sum_out += sum_tempo
        print(f'сумма введенных чисел равна {sum_tempo}')
        print(f'кумулятивная сумма равна {sum_out}')
        if flag_out:break



'''Реализовать функцию int_func(), принимающую слово 
из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, 
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().'''

def int_func(inp_word):
    return inp_word.replace(inp_word[0], chr(ord(inp_word[0]) - 32))

def n6(Inp_str):
    inp_list = Inp_str.split(' ')
    out_str=''
    for world in inp_list:
        out_str+=int_func(world)+' '
    return(out_str)



def run(number):
    if number==1:
        while True:
            try:
                x1, x2 = input('Введите через запятую любые два числа- ').split(',')
                print(f'результат деления чисел {x1} и {x2} равен => {n1(float(x1), float(x2))}')
                break
            except ValueError:
                print('Введите корректные данные')
            except:
                continue
    elif number == 2:
       print(n2(first_nam='Ivan', last_name='Ivanov', year=2000, city='tula', mail='ivanov_tula@mail.ru', phone_number=9374304561))
    elif number==3:
        print(f'Сумма двух наибольших чисел равна {n3(15,-30,10)} ')
    elif number==4:
        foundation=7
        degree = -5
        classic, my = n4(foundation,degree)
        print(f'{foundation} в степени {degree} равно (встроенная функция) => {classic}')
        print(f'{foundation} в степени {degree} равно (моя функция) => {my}')
    elif number == 5:
        n5()
    elif number == 6:
        inp_str='the elephant went for a walk'
        print(inp_str)
        print(n6( inp_str))




if __name__=='__main__':
    run(6)