# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def total_income(self):
        print(self._income['wage'] + self._income['bonus'])


if __name__ == '__main__':
    doctor = Position('Will', 'Smith', 'actor', 2000, 3000)
    doctor.get_full_name()
    doctor.total_income()
    print(doctor.position)
    print(20 * '-')
    layer = Position('Bob', 'Trump', 'CIO', 1000)
    layer.get_full_name()
    layer.total_income()
    print(layer.position)
    layer.name = 'Ivan'
    layer.total_income()
    layer.get_full_name()