from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observers.subject import Subject


class Observer(ABC):
    
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        pass
