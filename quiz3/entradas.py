from entrada_base import EntradaBase

class General(EntradaBase):
    def __init__(self, cant_personas: int, evento: str):
        self.cant_personas = cant_personas
        self.evento = evento
        self.precio_base = 10000  # Precio por persona en colones

    def calcular_precio(self):
        return self.precio_base * self.cant_personas

    def obtener_descripcion(self):
        return f"Entrada General para {self.evento} - {self.cant_personas} persona(s)"


class VIP(EntradaBase):
    def __init__(self, cant_personas: int, evento: str):
        self.cant_personas = cant_personas
        self.evento = evento
        self.precio_base = 25000

    def calcular_precio(self):
        return self.precio_base * self.cant_personas

    def obtener_descripcion(self):
        return f"Entrada VIP para {self.evento} - {self.cant_personas} persona(s)"


class Estudiante(EntradaBase):
    def __init__(self, cant_personas: int, evento: str):
        self.cant_personas = cant_personas
        self.evento = evento
        self.precio_base = 7000

    def calcular_precio(self):
        return self.precio_base * self.cant_personas

    def obtener_descripcion(self):
        return f"Entrada Estudiante para {self.evento} - {self.cant_personas} persona(s)"


class Grupo(EntradaBase):
    def __init__(self, cant_personas: int, evento: str):
        self.cant_personas = cant_personas
        self.evento = evento
        self.precio_base = 8500 

    def calcular_precio(self):
        return self.precio_base * self.cant_personas

    def obtener_descripcion(self):
        return f"Entrada Grupal para {self.evento} - {self.cant_personas} persona(s)"
