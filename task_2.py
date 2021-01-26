"""
Создайте класс Ship, который содержит информацию о корабле.
С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые для работы методы.
"""


class Ship():
    """Класс описывающий корабль"""

    def __init__(self, length: float, name: str, displacement: float):
        self._length = length
        self._name = name
        self._displacement = displacement


class Frigate(Ship):
    """Класс описывающий фрегат"""

    def __init__(self, number_of_guns: int):
        super().__init__()
        self._number_of_guns = number_of_guns


class Cruiser(Ship):
    """Класс описывающий крейсер"""

    def __init__(self):
        super().__init__()


class Destroyer(Ship):
    """Класс описывающий эсминец"""

    def __init__(self):
        super().__init__()