from src.models.item import Item

class HealingPotion(Item):
    def __init__(self, amount=20):
        self.amount = amount

    def use(self, user):
        user.heal(self.amount)
        return f"{user.name} usa pocion de curacion restaurando {self.amount} de salud"

    def on_critical(self, user, current_message: str):
        bonus_heal = 10
        user.heal(bonus_heal)
        return current_message + f" CURACION CRITICA +{bonus_heal} salud extra"
