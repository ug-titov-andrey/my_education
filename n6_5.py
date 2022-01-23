'''Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self, Title):
        self.title=Title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, Title, Type):
        self.type=Type
        Stationery.__init__(self,Title)
    def draw(self):
        Stationery.draw(self)
        print(f'{self.type} {self.title} пишет\n _______________________________')
class Pencil(Stationery):
    def __init__(self, Title, Type):
        self.type=Type
        Stationery.__init__(self,Title)
    def draw(self):
        Stationery.draw(self)
        print(f'{self.type} {self.title} рисует\n _______________________________')

class Handle(Stationery):
    def __init__(self, Title, Color):
        self.color=Color
        Stationery.__init__(self,Title)
    def draw(self):
        Stationery.draw(self)
        print(f'{self.color} {self.title} выделяет нужные фрагменты \n _______________________________')

if __name__=='__main__':
    my_stationery=[Pen('шариковая', 'ручка'), Pencil('цветной', 'карандаш'),Handle('желтый', 'маркер')]

    for stationery in my_stationery:
        stationery.draw()