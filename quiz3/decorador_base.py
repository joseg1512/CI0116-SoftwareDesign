from entrada_base import EntradaBase

class DecoradorBase(EntradaBase):
    def __init__(self, entrada_base: EntradaBase):
        self._entrada_base = entrada_base

    def calcular_precio(self):
        return self._entrada_base.calcular_precio()

    def obtener_descripcion(self):
        return self._entrada_base.obtener_descripcion()
