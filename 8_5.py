'''
. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
 Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
  Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
'''
import math

from my_exc import My_exception

class My_complex:
    def __init__(self, a, b):
        self.real = a
        self.im = b

    def get_complex(self):
        return (self._real, self.im)

    def set_complex(self, a, b):
        try:
            self.real = float(a)
            self._im = float(b)
        except ValueError:
            raise My_exception('Должно быть число')

    def get_abs(self):
        return math.sqrt(self.real ** 2 + self.im ** 2)

    def __add__(self, other):
        return My_complex(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        real = self.real * other.real - self.im * other.im
        im = self.real * other.im + self.im * other.real
        return My_complex(real, im)

    def __str__(self):
        return f'{self.real} +  {self.im} i' if self.im >= 0 else f'{self.real} -   {math.fabs(self.im)} i'


A = My_complex(2, 5)
B = My_complex(10, -30)
print(f'({A}) + ({B}) = ({A + B})')
print(f'({A}) * ({B}) = ({A * B})')







