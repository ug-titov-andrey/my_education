'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
 «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен
 извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
  должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
  структуры на реальных данных.     day, month, year
'''
from my_exc import My_exception
class Date:
    list_date=['день','месяц','год']

    def __init__(self, str_date):
        Date.str_date=str_date

    @classmethod
    def get_date(cls):
        out_date=[]
        tempo_date = cls.str_date.split('-')
        for ind,value in enumerate(tempo_date):
            value=Date.check_date(value,cls.list_date[ind])
            out_date.append(value)
        return out_date
    @staticmethod
    def check_date(number,date):
        if number.isdigit():
            value = int(number)
            if date=='день' and value > 31:
                raise  My_exception('День месяца не бывает  больше, чем 31')
            if date=='месяц' and value > 12:
                raise  My_exception(f'Не бываeт {number} месяца')
            if date=='год' and   (value <  0 or value > 2022):
                raise  My_exception(f'Не корректный год')
        else:
            raise My_exception(f'{date} из строки входных данных должен быть числом')
        return value

if __name__=='__main__':
    a = input('введите дату в формате день-месяц-год - ')
    date=Date(a)
    try:
        my_date=Date.get_date()
        for val in my_date:
            print(val)
    except My_exception as e:
        print(e)
