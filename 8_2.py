'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

from my_exc import My_exception


if __name__=='__main__':
    a=None
    b=None
    while True:
        if a==None:
            try:
                a = int(input('Введите число (числитель): '))
            except ValueError:
                a=None
                print('Введенная строка должна быть числом')
                continue
        if b==None:
            try:
                b = int(input('Введите число (знаменатель): '))
                if b==0: raise(My_exception('Знаменатель не может быть равен нулю'))
                break
            except ValueError:
                b=None
                print('Введенная строка должна быть числом')
                continue
            except My_exception as e:
                b=None
                print(e)
                continue
    print(f'результат деления числа {a} на число {b} равен => {a/b} ')







