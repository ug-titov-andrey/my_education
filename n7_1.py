'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''
import math
class My_exception(Exception):
    def __init__(self,report):
        self.report=report
    def __str__(self):
        return self.report

class Matrix:
    def __init__(self, list_data):
        self.max_number =0
        self.nrows=0
        self.ncols=0
        self.matr = self.convert_for_int(list_data)
    def convert_for_int(self, my_matr):
        max_value=0
        for ind, y in enumerate(my_matr):
            try:
                my_matr[ind] = list(map(int, y))
                tempo = max(list(map(abs, my_matr[ind])))
                if max_value < tempo: max_value = tempo
            except (ValueError, TypeError):
                raise My_exception('Ошибка произошла при преобразовании элементов списка к целым числам')
            else:
                self.nrows=ind+1
                self.ncols=len(my_matr)
        self.set_max_number(max_value)
        return my_matr
    def set_max_number(self, max_value):
        tempo_numb=0
        while True:
            max_value = math.trunc(max_value / 10)
            tempo_numb+=1
            if max_value == 0: break
        self.max_number =tempo_numb
    def __str__(self):
        out_str=''
        n=self.max_number+2
        for y in self.matr:
            out_str +='|'
            for x in y:
                out_str+='%-*d'%(n,x)

            out_str +='|\n'
        return out_str
    def __add__(self, other):
        sum_matr=[]
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise My_exception('Число строк и столбцов в суммируемых матрицах должно совпадать')
        else:
            for y in range(self.nrows):
                sum_matr.append(list(map(lambda x: self.matr[y][x]+other.matr[y][x],  range(self.ncols))))
        return Matrix(sum_matr)


if __name__=='__main__':
    try:
        A=Matrix([['-990', '-3', '7'],['8', '1776', '21'],['24', '-30', '298']])
        B=Matrix([['-183', '39', '-54'], ['-3', '25', '-102'], ['37', '21', '11006']])
        C=A+B
        print(C)
    except My_exception as e:
        print(e)



