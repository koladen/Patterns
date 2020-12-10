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