# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def asphalt_mass(self, density: int, depth: int):
        print(f'Will require {self._width * self._length * density * depth / 1000} Tones of asphalt')


if __name__ == '__main__':
    road_to_hell = Road(length=666, width=13)
    road_to_hell.asphalt_mass(25, 5)

