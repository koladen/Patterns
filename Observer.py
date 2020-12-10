from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError()

    @abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError()

    @abstractmethod
    def notify_observers(self):
        raise NotImplementedError()


class Observer(ABC):

    def update(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.display()

    @abstractmethod
    def display(self):
        raise NotImplementedError()


class WeatherData(Subject):
    def __init__(self):
        self.observers = set()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.discard(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(temperature=self.temperature, humidity=self.humidity, pressure=self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentDisplay(Observer):
    def display(self):
        print('текущее значение показателей: ')
        for indicator, value in vars(self).items():
            print(indicator + ' = ' + value)


class StatisticDisplay(Observer):
    def display(self):
        print('Статистика за период по показателям: ')
        for indicator, value in vars(self).items():
            print(indicator + ' = ' + value)


my_display = CurrentDisplay()
stat_display = StatisticDisplay()

weather = WeatherData()
weather.register_observer(my_display)
weather.register_observer(stat_display)
weather.set_measurements(temperature='-7', humidity='70%', pressure='220mm')
weather.remove_observer(my_display)
weather.set_measurements(temperature='12', humidity='40%', pressure='200mm')
