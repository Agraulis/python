# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    traffic_light_param = {'red': 7, 'yellow': 2, 'green': 1}

    def set_color(self, color):
        if not (color in TrafficLight.traffic_light_param.keys()):
            print('There is no such color in traffic lights. Set to green by default.')
            color = 'green'
        self.__color = color
        self.__switch_time = TrafficLight.traffic_light_param[color]

    def __init__(self, color='green'):
        if not (color in TrafficLight.traffic_light_param.keys()):
            print('There is no such color in traffic lights. Set to green by default.')
            color = 'green'
        self.__color = color
        self.__switch_time = TrafficLight.traffic_light_param[color]

    def __next_color(self, current_color):
        if current_color == 'red':
            self.__color = 'yellow'
        elif current_color == 'yellow':
            self.__color = 'green'
        self.__switch_time = TrafficLight.traffic_light_param[self.__color]

    def running(self):
        colors = TrafficLight.traffic_light_param.keys()

        for color in colors:
            if self.__color == color:
                for sec in range(self.__switch_time):
                    print(f'Color is {self.__color}. {self.__switch_time - sec} seconds to switch.')
                    sleep(1)
                self.__next_color(self.__color)
                print(40 * '-')


if __name__ == '__main__':
    a = TrafficLight('red')
    # a.set_color('yellow')
    a.running()

