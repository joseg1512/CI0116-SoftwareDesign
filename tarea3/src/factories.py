from pedido import Pedido

class CreadorHamburguesas:
    def crear_pedido(self, id_pedido):
        return Pedido(id_pedido, "Hamburguesa")

class CreadorPizzas:
    def crear_pedido(self, id_pedido):
        return Pedido(id_pedido, "Pizza")
