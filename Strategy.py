"""
Стратегия — это поведенческий паттерн проектирования, который определяет семейство схожих алгоритмов и помещает каждый
из них в собственный класс, после чего алгоритмы можно взаимозаменять прямо во время исполнения программы.
Паттерн Стратегия предлагает определить семейство схожих алгоритмов, которые часто изменяются или расширяются, и
вынести их в собственные классы, называемые стратегиями. Вместо того, чтобы изначальный класс сам выполнял тот или
иной алгоритм, он будет играть роль контекста, ссылаясь на одну из стратегий и делегируя ей выполнение работы. Чтобы
сменить алгоритм, вам будет достаточно подставить в контекст другой объект - стратегию.
Применимость:
Когда вам нужно использовать разные вариации какого-то алгоритма внутри одного объекта. С тратегия позволяет варьировать
поведение объекта во время выполнения программы, подставляя в него различ-ные объекты-поведения (например, отличающиеся
балансом скорости и потребления ресурсов).
Когда у вас есть множество похожих классов, отличающих-ся только некоторым поведением.
С тратегия позволяет вынести отличающееся поведение в отдельную иерархию классов, а затем свести первоначальные классы к
одному , сделав поведение этого класса настраиваемым.
Когда различные вариации алгоритмов реализованы в виде развесистого условного оператора. Каждая ветка такого оператора
представляет собой вариацию алгоритма. С тратегия помещает каждую лапу такого оператора в отдельный класс - стратегию.
Затем контекст получает определённый объект - стратегию от клиента и делегирует ему работу . Если вдруг понадобится
сменить алгоритм, в контекст можно подать другую стратегию.
Недостатки:
1) У сложняет программу за счёт дополнительных классов.
2) Клиент должен знать, в чём состоит разница между стратегиями, чтобы выбрать подходящую.
"""

from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('Лечу на крыльях любви!')


class FlyNoFly(FlyBehavior):
    def fly(self):
        print('Рожденный ползать - летать не может!')


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError()


class QuackYell(QuackBehavior):
    def quack(self):
        print('Кваканье разносилось на километры вокруг')


class QuackSilence(QuackBehavior):
    def quack(self):
        print('Тише воды, ниже травы')


class Duck(ABC):
    def __init__(self, fly_behavior=FlyWithWings, quack_behavior=QuackYell):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior().fly()

    def perform_quack(self):
        self.quack_behavior().quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.fly_behavior = quack_behavior

    @abstractmethod
    def display(self):
        raise NotImplementedError()


class DuckVulgaris(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyWithWings, quack_behavior=QuackYell)

    def display(self):
        print('Я - обыкновенная утка!')
        self.perform_fly()
        self.perform_quack()


class Pingvin(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyNoFly, quack_behavior=QuackYell)

    def display(self):
        print('Я - пингвин!')
        self.perform_fly()
        self.perform_quack()


class Manok(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyNoFly, quack_behavior=QuackSilence)

    def display(self):
        print('Я - деревянный манок!')
        self.perform_fly()
        self.perform_quack()


duck = DuckVulgaris()
duck.display()
duck.set_fly_behavior(FlyNoFly)
duck.display()

manok = Manok()
manok.display()

pingvin = Pingvin()
pingvin.display()
