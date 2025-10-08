import threading
import queue
import time

class ServicioPedidos:
    def __init__(self, num_cocineros=2):
        self.cola_pedidos = queue.Queue()
        self.num_cocineros = num_cocineros

    def agregar_pedido(self, pedido):
        self.cola_pedidos.put(pedido)

    def procesar_pedidos(self):
        threads = []
        for i in range(self.num_cocineros):
            t = threading.Thread(target=self._cocinero, args=(i + 1,))
            t.start()
            threads.append(t)

        self.cola_pedidos.join()

        for _ in range(self.num_cocineros):
            self.cola_pedidos.put(None)
        for t in threads:
            t.join()

        print("[SISTEMA] Todos los pedidos procesados")

    def _cocinero(self, id_cocinero):
        while True:
            pedido = self.cola_pedidos.get()
            if pedido is None:
                break
            print(f"[COCINERO {id_cocinero}] Preparando pedido {pedido.id_pedido} ({pedido.tipo})")
            print(f"[COCINERO {id_cocinero}] Pedido {pedido.id_pedido} listo: {pedido.preparar()}")
            self.cola_pedidos.task_done()
