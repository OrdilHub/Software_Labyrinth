from abc import ABCMeta, abstractmethod


class ICell(metaclass=ABCMeta):
    @abstractmethod
    def get_cellType(self):pass
