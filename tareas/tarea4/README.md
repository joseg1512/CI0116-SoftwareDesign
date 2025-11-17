# Tarea 4
## Jose Gabriel Granados Duarte - C33468

## Patrones de Diseño Implementados

### 1. Patrón Decorator

El problema principal era permitir que los clientes personalicen productos con ingredientes extras (leche, canela, crema, etc.). Usar herencia habría requerido crear una clase para cada combinación posible (CaféConLeche, CaféConLecheYCanela, CaféConLecheYCanelaYCrema, etc.), lo cual es inviable.

Con el patrón Decorator se resuelve esto permitiendo que los extras se agregan en tiempo de ejecución envolviendo el producto base:

- **Combinaciones:** `Cinnamon(Milk(Coffee()))` crea un café con leche y canela
- **Cálculo automático:** Cada decorador suma su precio al total
- **Extensibilidad:** Agregar nuevos extras solo requiere crear una nueva clase decoradora

**Ejemplo en el código:**
```python
coffee = Cinnamon(Milk(Coffee()))  # Café con leche y canela
print(coffee.get_description())     # "Coffee with milk with cinnamon"
print(coffee.get_price())           # 3.30 (2.5 + 0.5 + 0.3)
```

### 2. Patrón Observer

El sistema necesita notificar a los clientes cuando sus pedidos están listos. El patrón obsever evita hacer esto en la clase `Order`, lo que crearía un acoplamiento fuerte y haría difícil extender el sistema.

El patrón Observer lo resuelve de la siguiente manera:
- **Desacoplamiento:** `Order` no necesita conocer los detalles de `Customer`
- **Suscripción automática:** Los clientes se suscriben a sus pedidos y reciben notificaciones automáticamente
- **Extensibilidad:** Se pueden agregar nuevos observadores (sistema de cocina, inventario) sin modificar `Order`
- **Notificación:** Se notifica cuando el estado cambia a "Ready"

**Flujo en el código:**
1. Se crea un pedido y el cliente se suscribe automáticamente
2. Cuando el pedido cambia a estado "Ready", llama a `notify()`
3. Todos los observadores suscritos reciben la actualización con `update()`

## Decisiones de diseño

- Se organizó el código en módulos (`app/`, `models/`, `observers/`) para separar responsabilidades y facilitar el mantenimiento. Cada módulo tiene un propósito definido.

- En `Cafeteria.create_order()`, el cliente se suscribe automáticamente a su pedido. Esto permite evitar errores como que al cliente se olvide de suscribirse a su pedido y simplifica el uso del sistema.

- `Order` solo notifica a los observadores cuando el estado cambia a "Ready", evitando notificaciones innecesarias en otros cambios de estado.

## Principios SOLID Aplicados

- **Single Responsibility:** Cada clase tiene una única responsabilidad bien definida
- **Open/Closed:** Se pueden agregar nuevos productos, decoradores y observadores sin modificar código existente
- **Liskov Substitution:** Los decoradores y productos concretos son intercambiables con la interfaz base
- **Interface Segregation:** Interfaces pequeñas y específicas (Observer, Subject, Product)
- **Dependency Inversion:** Las clases dependen de abstracciones, no de implementaciones concretas

## Ejecución

```bash
python main.py
```