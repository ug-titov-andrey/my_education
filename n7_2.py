'''2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
 размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''
from abc import ABCMeta, abstractmethod
class My_exception(Exception):
    def __init__(self, err_str):
        self.err_str=err_str
    def __str__(self):
        return self.err_str
class Clothes(metaclass=ABCMeta):

    def __init__(self, name=None):
        self.name=name
    @abstractmethod
    def get_material(self):
        pass
class Coat(Clothes):
    def __init__(self, v):
        self.v=v
        Clothes.__init__(self, 'пальто')
    @property
    def v(self):
        return self._v
    @v.setter
    def V(self, v):
        try:
            self._v=float(v)
        except:
            raise My_exception('Размер должен быть числом')
        else:
            if self._v <=0:  raise My_exception('Размер должен быть положительным числом')
    def get_material(self):
        return self.v/6.5 + 0.5


class Coat(Clothes):
    def __init__(self, v):
        self.v=v
        Clothes.__init__(self, 'пальто')
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, v):
        try:
            self._v=float(v)
        except:
            raise My_exception('Размер должен быть числом')
        else:
            if self._v <=0:  raise My_exception('Размер должен быть положительным числом')
    def get_material(self):
        return self.v/6.5 + 0.5
class Suit(Clothes):
    def __init__(self, h):
        self.h=h
        Clothes.__init__(self, 'костюм')
    @property
    def h(self):
        return self._h
    @h.setter
    def h(self, h):
        try:
            self._h=float(h)
        except:
            raise My_exception('Рост должен быть числом')
        else:
            if self._h <=0:  raise My_exception('Рост должен быть положительным числом    ')
    def get_material(self):
        return 2*self.h + 0.3

if __name__ == '__main__':
    try:
        my_coat = Coat('123')
        my_coat.v=19
        print(f'Размер {my_coat.name} равен {my_coat.v}. На его пошив ушло {my_coat.get_material()} ткани')
        my_suit = Suit(180)
        my_suit.h = 178
        print(f'Рост {my_suit.name}а равен {my_suit.h}. На его пошив ушло {my_suit.get_material()} ткани')
        print('finish')


    except My_exception as x:
        print(x)
