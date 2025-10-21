import unittest
from unittest.mock import MagicMock

from src.app.combat_system import CombatSystem
from src.app.item_system import ItemSystem
from src.models.character import Character
from src.models.weapon import Weapon
from src.models.strength_potion import StrengthPotion


class TestStrengthPotion(unittest.TestCase):

    class FakeWeapon(Weapon):
        def __init__(self, base=15):
            self.base = base

        def attack(self, attacker, target):
            bonus = getattr(attacker, 'damage_bonus', 0)
            damage = self.base + bonus
            target.take_damage(damage)
            return f"{attacker.name} golpea causando {damage} de dano"

    def test_strength_potion_increases_damage_by_10(self):
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = False

        items = ItemSystem(mock_calculator)
        combat = CombatSystem(mock_calculator)

        hero = Character("Hero")
        enemy = Character("Enemy")
        potion = StrengthPotion()

        items.use_item(hero, potion)
        weapon = self.FakeWeapon(base=15)

        combat.perform_attack(hero, weapon, enemy)

        # 15 base + 10 de la poción = 25
        self.assertEqual(enemy.health, 75)

    def test_strength_potion_stacks_with_critical(self):
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = True

        items = ItemSystem(mock_calculator)
        combat = CombatSystem(mock_calculator)

        hero = Character("Hero")
        enemy = Character("Enemy")
        potion = StrengthPotion()

        items.use_item(hero, potion)
        weapon = self.FakeWeapon(base=15)

        combat.perform_attack(hero, weapon, enemy)

        # 15 base + 10 poción + 10 crítico = 35
        self.assertEqual(enemy.health, 65)
