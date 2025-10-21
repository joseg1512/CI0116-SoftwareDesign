import unittest
from unittest.mock import MagicMock

from src.app.item_system import ItemSystem
from src.models.character import Character
from src.models.healing_potion import HealingPotion


class TestItemSystem(unittest.TestCase):

    def test_item_system_uses_injected_calculator(self):
        """ItemSystem usa la calculadora inyectada"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = False

        items = ItemSystem(mock_calculator)
        hero = Character("Hero")
        potion = HealingPotion(amount=15)

        items.use_item(hero, potion)

        mock_calculator.check_critical_hit.assert_called_once()

    def test_critical_heal_adds_extra_heal(self):
        """La curación crítica agrega curación extra"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = True

        items = ItemSystem(mock_calculator)
        hero = Character("Hero", health=50)
        potion = HealingPotion(amount=20)

        result = items.use_item(hero, potion)

        # 50 + 20 de la poción + 10 de crítico = 80
        self.assertEqual(hero.health, 80)
        self.assertIn("CURACION CRITICA", result)

    def test_cannot_use_item_when_user_is_dead(self):
        """No se debe usar el ítem si el objetivo está derrotado"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = True

        items = ItemSystem(mock_calculator)
        hero = Character("Hero")
        hero.take_damage(200)  # queda derrotado
        potion = HealingPotion(amount=20)

        result = items.use_item(hero, potion)

        self.assertIn("derrotado", result)
        # Salud no cambia al intentar usar ítem
        self.assertEqual(hero.health, 0)
