"""
Создайте класс Device, который содержит информацию об устройстве. С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине), класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).Каждый из классов должен содержать необходимые
для работы методы.
"""


class Device:
    """Устройство реализующее функционал автоматизации процессов"""
    button: bool = False

    @classmethod
    def on_off(cls):
        if cls.button:
            return False
        return True


class CoffeeMachine(Device):
    """Устройство для автоматизации процесса приготовления кофе"""

    def __init__(self, water: int, milk: int, coffee_beans: int, cups: int, money: int):
        self._water = water
        self._milk = milk
        self._coffee_beans = coffee_beans
        self._cups = cups
        self._money = money


class Blender(Device):
    """Устройство автомазирующее процесс замешивания продуктов"""
    def __init__(self, speed_count: int, capacity: int):
        self._speed_count = speed_count
        self._capacity = capacity


class MeatGrinder(Device):
    """Устройство автоматизурующее процесс изготовления мясного фарша"""

    def __init__(self, power: int, capacity: int):
        self._power = power
        self._capacity = capacity



