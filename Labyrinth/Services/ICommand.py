from abc import *


class ICommand(metaclass = ABCMeta):

    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def get_args_count(self): pass

    @abstractmethod
    def evaluate(self, args, labyrinth, player): pass