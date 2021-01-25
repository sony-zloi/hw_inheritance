"""
Создайте класс Ship, который содержит информацию о корабле.
С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые для работы методы.
"""


class Ship(object):
    def __init__(self, length, name):
        self.length = length
        self.name = name


class Frigate(Ship):
    pass


class Cruiser(Ship):
    pass


class Destroyer(Ship):
    pass