from abc import ABCMeta, abstractmethod


class ILabyrinth(metaclass=ABCMeta):
    @abstractmethod
    def get_size(self):pass
    @abstractmethod
    def get_entry(self):pass
    @abstractmethod
    def view(self):pass
    @abstractmethod
    def get_specialRooms(self):pass