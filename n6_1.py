'''1. Создать класс TrafficLight (светофор).
•	определить у него один атрибут color (цвет) и метод running (запуск);
•	атрибут реализовать как приватный;
•	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
•	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
•	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
•	проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time


class TrafficLight:
    color_delay = {'red': 7, 'yellow': 5, 'green': 2}
    def __init__(self, Order, Color='red'):
        self.order = Order
        self.__color = Color

    __color = None

    def running(self):
        keys_iter = iter(self.color_delay.keys())
        for value in self.order:
            my_color=next(keys_iter)
            if value == my_color:
                self.__color = value
                print(f'Зажегся {self.__color } цвет')
                time.sleep(self.color_delay[my_color])
            else:
                print('Светофор не работает')
                break


if __name__ == '__main__':
    order = ['red','yellow', 'green']
    trafficLight = TrafficLight(order)
    trafficLight.running()

