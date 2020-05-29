from abc import ABCMeta, abstractmethod

from Implementations.Labyrinth import Labyrinth


class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def get_Inventory(self):pass
    @abstractmethod
    def north(self,labyrinth:Labyrinth):pass
    @abstractmethod
    def west(self,labyrinth:Labyrinth):pass
    @abstractmethod
    def east(self,labyrinth:Labyrinth):pass
    @abstractmethod
    def south(self,labyrinth:Labyrinth):pass
    @abstractmethod
    def research(self):pass
