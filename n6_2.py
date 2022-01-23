''' Реализовать класс Road (дорога).
    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина*ширина*масса асфальта для покрытия одного
    кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
    проверить работу метода.
'''
class Road:
    m=25 #масса 1 кв. метра
    t=8 #толщина асфальтового слоя

    def __init__(self, Length, Width,):
        self._length=Length #длина дороги
        self._width=Width #ширина дороги

    def calc_all_mas(self):
        return self._width*self._length*self.t*self.m
    def __str__(self):
        return f'Маcса асфальта для строительства дороги равна => {self.calc_all_mas()} кг'

if __name__=='__main__':
    road = Road(30000,15)

    print(road)

