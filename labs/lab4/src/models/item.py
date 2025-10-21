from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def use(self, user):
        pass
