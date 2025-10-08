from servicio_pedidos import ServicioPedidos
from factories import CreadorHamburguesas, CreadorPizzas

if __name__ == "__main__":
    servicio = ServicioPedidos(num_cocineros=2)

    # Factory para hamburguesas
    creador_hamburguesas = CreadorHamburguesas()
    for i in range(3):
        pedido = creador_hamburguesas.crear_pedido(i)
        servicio.agregar_pedido(pedido)

    # Factory para pizzas
    creador_pizzas = CreadorPizzas()
    for i in range(3, 6):
        pedido = creador_pizzas.crear_pedido(i)
        servicio.agregar_pedido(pedido)

    servicio.procesar_pedidos()
