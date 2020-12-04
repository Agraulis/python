"""
2. Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""

import os


def print_directory_contents(sPath: str):
    current_cat = os.listdir(sPath)
    if not current_cat:
        return None
    for name in current_cat:
        if os.path.isdir(name):
            print(f'{name}:')
            print_directory_contents(sPath + f'/{name}')
        else:
            print(name)


if __name__ == '__main__':
    print_directory_contents(os.getcwd())


