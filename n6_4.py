'''''4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые
должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''
class Car:
    def __init__(self, Speed, Color, Name, Is_police):
        self.speed=Speed
        self.color = Color
        self.name = Name
        self.is_police = Is_police
    def go(self):
        print('Едем')
    def stop(self):
        print('Stop')
    def turn(self, direction):
        print(f'Повернули на{direction}')
    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed} км/час')

class SportCar(Car):
    def __init__(self, Speed, Color, Name):
        Car.__init__(self, Speed, Color, Name, False)
        print('Спортивная машина готова')

class PoliceCar(Car):
    def __init__(self, Speed, Color, Name):
        Car.__init__(self, Speed, Color, Name, True)
        print('Машина полиции готова')


class TownCar(Car):
    def __init__(self, Speed, Color, Name):
        Car.__init__(self, Speed, Color, Name, False)
        print('Трамвай готов')
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('Едем слишком быстро')
class WorkCar(Car):
    def __init__(self, Speed, Color, Name):
        Car.__init__(self, Speed, Color, Name, False)
        print('Готовы перевозить грузы')
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('Едем слишком быстро')

my_car=[WorkCar(50, 'желтая', 'Машина для перевозки грузов'), TownCar(65, 'синий', 'трамвай'), PoliceCar(90, 'в полоску', 'машина полиции'),SportCar(120, 'Черная', 'спортивная машина')]
print('________________________________________')
for car in my_car:
    car.show_speed()


