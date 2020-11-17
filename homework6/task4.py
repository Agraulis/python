# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.current_speed = 0
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        # если скорость меняется во время движения машины, то параметр current_speed тоже надо поменять
        if key == 'speed' and self.__dict__['current_speed']:
            self.__dict__['current_speed'] = value

    def go(self):
        print(f'The car {self.name} started.')
        self.current_speed = self.speed

    def turn(self, direction):
        print(f'The car {self.name} turned {direction}.')

    def stop(self):
        print(f'The car {self.name} stopped.')
        self.current_speed = 0

    def show_speed(self):
        print(f'The speed is {self.current_speed} km/h.')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'The speed is {self.current_speed} km/h.')
        if self.current_speed > 60:
            print('You are speeding!')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'The speed is {self.current_speed} km/h.')
        if self.current_speed > 40:
            print('You are speeding!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


if __name__ == '__main__':
    time_machine = SportCar(142, 'silver', 'DeLorean DMC-12')
    time_machine.go()
    time_machine.show_speed()
    time_machine.turn('left')
    time_machine.stop()
    time_machine.show_speed()
    print(20 * '-')
    taxi = TownCar(50, 'white', 'Peugeot')
    taxi.show_speed()
    taxi.go()
    taxi.show_speed()
    print(taxi.color)
    taxi.speed = 200
    taxi.show_speed()
    taxi.stop()
    print(20 * '-')


