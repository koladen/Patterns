"""
Команда — это поведенческий паттерн проектирования, который превращает запросы в объекты, позволяя передавать их как
аргументы при вызове методов, ставить запросы в очередь, логировать их, а также поддерживать отмену операций.
Недостатки:
1) У сложняет код программы из-за введения множества допол-нительных классов.
"""
from abc import ABC, abstractmethod


#  Накопитель команд. Можно реализовать накопитель, который будет хранить очередь команд, и при выполнении добавлять
#  их в отдельный список выполненных команд. При необходимости отмены изменений пройти по списку выполненных команд
#  и отменить их
class RemoteController:
    def __init__(self):
        self.on_command = []
        self.off_command = []
        self.last_command = None

    def set_command(self, slot, command_on, command_off):
        self.on_command.insert(slot, command_on)
        self.off_command.insert(slot, command_off)

    def on_button_was_pushed(self, slot):
        self.on_command[slot].execute()
        self.last_command = self.on_command[slot]

    def off_button_was_pushed(self, slot):
        self.off_command[slot].execute()
        self.last_command = self.off_command[slot]

    def undo_button_was_pushed(self):
        self.last_command.undo()


class Light:
    def __init__(self, place):
        self.place = place

    def on(self):
        print(f'Свет включен в {self.place}')

    def off(self):
        print(f'Свет выключен в {self.place}')


# Команда. В команде ссылка на конкретный объект. Вместо команды можно использовать функцию, в функции реализовать всю
# логику, а в классе RemoteController переделать вызов self.on_command[slot].execute() на self.on_command[slot]()
class Command(ABC):
    def __init__(self, object_to_command):
        self.object_to_command = object_to_command

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def undo(self):
        raise NotImplementedError


class MacroCommand(Command):
    def __init__(self, command_list):
        super().__init__(command_list)

    def execute(self):
        for command in self.object_to_command:
            command.execute()

    def undo(self):
        for command in self.object_to_command:
            command.undo()


class LightOnCommand(Command):
    def __init__(self, object_to_command):
        super().__init__(object_to_command)

    def execute(self):
        self.object_to_command.on()

    # Реализация команды отмены самая простая. Тут можно наворотить все что угодно, запоминать состояния и тд  и тп
    def undo(self):
        self.object_to_command.off()


class LightOffCommand(Command):
    def __init__(self, object_to_command):
        super().__init__(object_to_command)

    def execute(self):
        self.object_to_command.off()

    def undo(self):
        self.object_to_command.on()


my_remote = RemoteController()
living_room_light = Light('Гостинная')
kitchen_light = Light('Кухня')

living_room_light_on = LightOnCommand(living_room_light)
living_room_light_off = LightOffCommand(living_room_light)

kitchen_light_on = LightOnCommand(kitchen_light)
kitchen_light_off = LightOffCommand(kitchen_light)

all_light_on = [living_room_light_on, kitchen_light_on]
all_light_off = [living_room_light_off, kitchen_light_off]

macro_on = MacroCommand(all_light_on)
macro_ff = MacroCommand(all_light_off)
my_remote.set_command(0, macro_on, macro_ff)
my_remote.on_button_was_pushed(0)
my_remote.undo_button_was_pushed()
# my_remote.off_button_was_pushed(0)

# my_remote.set_command(0, living_room_light_on, living_room_light_off)
# my_remote.set_command(1, kitchen_light_on, kitchen_light_off)
#
# my_remote.on_button_was_pushed(0)
# my_remote.on_button_was_pushed(1)
# my_remote.off_button_was_pushed(1)
# my_remote.undo_button_was_pushed()
# my_remote.off_button_was_pushed(0)
