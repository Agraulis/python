# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
from numpy import mean


class Employee:
    def __init__(self, name=None, salary=None, poor_border=20000):
        self.name = name
        self.salary = salary
        self.poor_border = poor_border
        self.poor_employee_detector(poor_border)

    def poor_employee_detector(self, poor_border):
        if self.salary < poor_border:
            print(f'{self.name} has a salary less than {poor_border}')


group_salary = []
with open('text_file_for_task3.txt', encoding='utf-8') as file:
    for line in file:
        second_name, his_salary = tuple(line.split('\t'))
        group_salary.append(Employee(second_name, float(his_salary)).salary)
print(f'Average employee salary is {mean(group_salary):.2f}')
