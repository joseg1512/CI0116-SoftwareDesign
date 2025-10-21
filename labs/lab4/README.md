# Lab 4
## Jose Gabriel Granados - C33468

## Items
- Se incorporó un sistema simple para que un personaje use ítems sobre sí mismo.
  - ItemSystem recibe por inyección una damage_calculator y expone `use_item(user, item)`.
  - Cada ítem implementa `use(user)`. Opcionalmente, puede definir `on_critical(user, message)` para reaccionar a golpes críticos.

## Ítems implementados
- HealingPotion (curación)
  - `use(user)`: cura una cantidad fija (20 por defecto).
  - `on_critical(user, message)`: si hay crítico, añade +10 de curación.

- StrengthPotion (fuerza)
  - `use(user)`: incrementa un atributo en user.damage_bonus en +10 por uso.

## Diseño
- Inyección de dependencias: ItemSystem no conoce implementaciones concretas; solo pide una calculadora de críticos para permitir casos de uso como curación crítica.
- Los ítems encapsulan su comportamiento; ItemSystem delega el crítico al ítem si lo soporta via on_critical.

## Tests agregados

  - `test_item_system_uses_injected_calculator`: valida que ItemSystem consulta la calculadora inyectada (mock) al usar un ítem.
  - `test_critical_heal_adds_extra_heal`: con crítico forzado (mock), HealingPotion aplica +10 adicional.
  - `test_cannot_use_item_when_user_is_dead`: si el usuario está derrotado, no permite usar ítems ni cambiar salud.

  - `test_strength_potion_increases_damage_by_10`: tras usar una vez la poción de fuerza, un ataque hace +10 daño (se verifica la salud restante del objetivo).
  - `test_strength_potion_stacks_with_critical`: el +10 de fuerza se suma con el +10 de crítico (se verifica la suma total).

Los tests de fuerza usan un arma Fake para sumar damage_bonus al daño base y aplicar el daño al objetivo, sin tocar las armas existentes

## Cómo correr los tests
- Desde labs/lab4:
  - py -m unittest discover -v .


