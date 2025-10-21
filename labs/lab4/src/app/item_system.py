class ItemSystem:
    def __init__(self, damage_calculator):
        self.damage_calculator = damage_calculator

    def use_item(self, user, item):
        if not user.is_alive:
            return f"{user.name} ya esta derrotado"

        result = item.use(user)
        # Aplicar crítico si lo soporta el item
        if self.damage_calculator.check_critical_hit() and hasattr(item, 'on_critical'):
            result = item.on_critical(user, result)

        return result
