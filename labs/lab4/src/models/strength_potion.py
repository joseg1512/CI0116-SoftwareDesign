from src.models.item import Item

class StrengthPotion(Item):
    """Poción de fuerza: cada uso aumenta el daño en +10 de forma indefinida."""

    def __init__(self, increment: int = 10):
        self.increment = increment

    def use(self, user):
        current = getattr(user, 'damage_bonus', 0)
        new_bonus = current + self.increment
        setattr(user, 'damage_bonus', new_bonus)
        return (
            f"{user.name} usa pocion de fuerza: +{self.increment} dano"
        )

