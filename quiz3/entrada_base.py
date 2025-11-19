from abc import ABC, abstractmethod

class EntradaBase(ABC):

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass