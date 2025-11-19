from entrada_base import EntradaBase
from decorador_base import DecoradorBase

class DescuentoEstudiante(DecoradorBase):
    def __init__(self, entrada_base: EntradaBase, descuento: float = 0.15):
        super().__init__(entrada_base)
        self.descuento = descuento

    def calcular_precio(self):
        precio_original = self._entrada_base.calcular_precio()
        return precio_original * (1 - self.descuento)

    def obtener_descripcion(self):
        return f"{self._entrada_base.obtener_descripcion()} + Descuento Estudiante ({self.descuento*100}%)"


class PromocionEspecial(DecoradorBase):
    def __init__(self, entrada_base: EntradaBase, descuento: float = 0.20):
        super().__init__(entrada_base)
        self.descuento = descuento

    def calcular_precio(self):
        precio_original = self._entrada_base.calcular_precio()
        return precio_original * (1 - self.descuento)

    def obtener_descripcion(self):
        return f"{self._entrada_base.obtener_descripcion()} + Promoción Especial ({self.descuento*100}%)"


class VIPDecorador(DecoradorBase):
    def __init__(self, entrada_base: EntradaBase, precio_adicional: float = 5000):
        super().__init__(entrada_base)
        self.precio_adicional = precio_adicional

    def calcular_precio(self):
        return self._entrada_base.calcular_precio() + self.precio_adicional

    def obtener_descripcion(self):
        return f"{self._entrada_base.obtener_descripcion()} + Upgrade VIP"
