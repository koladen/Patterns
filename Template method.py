"""
Шаблонный метод — это поведенческий паттерн проектирования, который определяет скелет алгоритма, перекладывая
ответственность за некоторые его шаги на подклассы. Паттерн позволяет подклассам переопределять шаги алгоритма, не меняя
его общей структуры.
Недостатки:
1) Вы жёстко ограничены скелетом существующего алгоритма.
2) Вы можете нарушить принцип подстановки Барбары Лис-ков, изменяя базовое поведение одного из шагов алгоритма
   через подкласс.
3) С ростом количества шагов шаблонный метод становится слишком сложно поддерживать.
"""

from abc import ABC, abstractmethod
import random


class Template(ABC):
    #  Это шаблон, который содержит в себе, как общие методы, так и те, которые нужно реализовать в наследниках.
    #  В шаблоне задается скелет алгоритма.
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_want_additions():
            self.add_additions()

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_additions(self):
        raise NotImplementedError

    def boil_water(self):
        print('Кипятим воду')

    def pour_in_cup(self):
        print('Наливаем в чашку')

    #  Это метод - перехватчик(hook) наследник может переопределить его, для выполнения каких-то целей
    def customer_want_additions(self):
        return True


class Cofee(Template):
    def brew(self):
        print('Варим кофе')

    def add_additions(self):
        print('Добавляем сахар и молоко')

    def customer_want_additions(self):
        if random.choice(range(1, 3)) == 2:
            return True
        else:
            return False


class Tea(Template):
    def brew(self):
        print('Завариваем чай')

    def add_additions(self):
        print('Добавляем лимон')


tea = Tea()
cofee = Cofee()
tea.prepare_recipe()
cofee.prepare_recipe()
