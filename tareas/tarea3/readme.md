# Sistema de Pedidos de Comida con Concurrencia
## Jose Gabriel Granados Duarte C33468

Programa para un sistema de gestión de pedidos de comida donde varios cocineros (threads) preparan pedidos de distintos tipos (hamburguesas y pizzas) de forma concurrente, aplicando el patrón Factory para crear los objetos de pedido.

### 1. Implementación del Patrón Factory


**Implementación:**
```python
class Pedido:
    def __init__(self, id_pedido, tipo):
        self.id_pedido = id_pedido
        self.tipo = tipo
```

Los factories crean instancias de esta clase con el tipo correspondiente:
```python
class CreadorHamburguesas:
    def crear_pedido(self, id_pedido):
        return Pedido(id_pedido, "Hamburguesa")

class CreadorPizzas:
    def crear_pedido(self, id_pedido):
        return Pedido(id_pedido, "Pizza")
```
Implementan el Patrón Factory, encapsulando la creación de distintos tipos de pedidos.
Esto permite agregar nuevos tipos sin modificar el código del servicio o del main.

### 2. Sistema de Concurrencia

La clase ServicioPedidos implementa una cola thread safe donde los pedidos se almacenan para ser procesados por varios cocineros (threads).
Cada cocinero ejecuta el método privado _cocinero(), que:

- Extrae pedidos de la cola.
- Simula su preparación.
- Marca el pedido como terminado (task_done()).

El método procesar_pedidos():
- Crea los hilos de cocineros.
- Espera que todos los pedidos se procesen (join()).
- Envía señales de finalización (None) a cada hilo.
- Imprime un mensaje cuando el sistema termina.

### 3. Sincronización 

- Se utiliza la clase queue.Queue, que es thread-safe.
- Esto garantiza que múltiples hilos puedan acceder y modificar la cola sin causar condiciones de carrera.
- Cada hilo trabaja sobre pedidos independientes, por lo que es necesario usar locks.
- El método join() asegura que el programa principal espere a que todos los pedidos sean procesados antes de finalizar.

## Cómo Ejecutar

```bash
python main.py
```
## Cómo Extender el Sistema

Para agregar un nuevo tipo de pedido:

1. Crear un nuevo factory en `factories.py`:
```python
class CreadorEnsaladas:
    def crear_pedido(self, id_pedido):
        return Pedido(id_pedido, "Ensalada")
```

2. Usar el factory en `main.py`:
```python
creador_ensaladas = CreadorEnsaladas()
for i in range(6, 9):
    pedido = creador_ensaladas.crear_pedido(i)
    servicio.agregar_pedido(pedido)
```

No se requiere modificar `pedido.py` ni `servicio_pedidos.py`.
