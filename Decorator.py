"""
Декоратор — это структурный паттерн проектирования, который позволяет динамически добавлять объектам новую
функциональность, оборачивая их в полезные «обёртки».
Применимость:
Когда вам нужно добавлять обязанности объектам на лету, незаметно для кода, который их использует.
Недостатки:
1) Трудно конфигурировать многократно обёрнутые объекты.
2) Обилие крошечных классов.
"""

from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        raise NotImplementedError


class Additions(ABC):
    def __init__(self, beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        raise NotImplementedError

    @abstractmethod
    def cost(self):
        raise NotImplementedError


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'Espresso'

    def cost(self):
        return 1.99


class Mocha(Additions):
    def __init__(self, beverage):
        super().__init__(beverage=beverage)

    def get_description(self):
        return self.beverage.get_description() + ' Mocha'

    def cost(self):
        return self.beverage.cost() + 0.20


class Whip(Additions):
    def __init__(self, beverage):
        super().__init__(beverage=beverage)

    def get_description(self):
        return self.beverage.get_description() + ' Whip'

    def cost(self):
        return self.beverage.cost() + 0.17


beverage = Espresso()
beverage = Mocha(beverage)
beverage = Mocha(beverage)
beverage = Whip(beverage)
print(beverage.get_description())
print(beverage.cost())