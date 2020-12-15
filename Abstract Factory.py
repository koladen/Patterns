"""
Это порождающий паттерн проектирования, который позволяет создавать семейства связанных объектов, не привязываясь к
конкретным классам объектов.
В данном случае, у нас есть абстрактная фабрика AbstractShop, которая в зависимости от наличия у клиентов денег,
порождает конкретные фабрики CheapShop и ExpensiveShop, у которых реализован метод bay_vkusnyashki, возвращающий
экземпляры классов наследников Beer и Snack.
Применимость: когда бизнес логика предполагает использовать разные виды связанных друг с другом продуктов, не завися
от конкретных классов продуктов.
Недостатки:
1) Усложняет код программы из-за введения множества дополнительных классов.
2) Требует наличия всех типов продуктов в каждой вариации.
"""

from abc import ABC, abstractmethod


class Beer(ABC):

    @abstractmethod
    def blow_off_foam(self):
        raise NotImplementedError()


class Klinskoe(Beer):
    def blow_off_foam(self):
        print('В Клинском пены мало...')


class Corona(Beer):
    def blow_off_foam(self):
        print('Сдул пол кружки, столько пены!')


class Snack(ABC):

    @abstractmethod
    def eat_snack(self):
        raise NotImplementedError()


class Arahis(Snack):
    def eat_snack(self):
        print('Мммм... солененький')


class Fua_gra(Snack):
    def eat_snack(self):
        print('Писец ее мало, а такая дорогая...')


class AbstractShop(ABC):

    @abstractmethod
    def bay_vkusnyashki(self):
        raise NotImplementedError()


class CheapShop(AbstractShop):
    def bay_vkusnyashki(self):
        beer = Klinskoe()
        snack = Arahis()
        return beer, snack


class ExpensiveShop(AbstractShop):
    def bay_vkusnyashki(self):
        beer = Corona()
        snack = Fua_gra()
        return beer, snack


got_many = int(input('Деньги есть? (1/0)'))
if got_many:
    factory = ExpensiveShop
else:
    factory = CheapShop

beer, snack = factory().bay_vkusnyashki()
beer.blow_off_foam()
snack.eat_snack()