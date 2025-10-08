class Pedido:
    def __init__(self, id_pedido, tipo):
        self.id_pedido = id_pedido
        self.tipo = tipo

    def preparar(self):
        return f"{self.tipo} {self.id_pedido} preparada"
