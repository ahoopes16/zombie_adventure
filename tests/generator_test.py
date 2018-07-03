"""This module contains a testing suite for the Random
Generator class.
@author: Kevin Hoopes
@version: 7/2/2018
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath('..'))
from src.random_generator import ItemGenerator, AmountGenerator, ItemAmountGenerator

class GeneratorTests(unittest.TestCase):

    """Hold the test cases for the Random Generator
    class."""

    def setUp(self):
        """Set up variables to run tests against."""
        self.item_gen = ItemGenerator()
        self.amount_gen = AmountGenerator()
        self.item_amount_gen = ItemAmountGenerator()
        self.encounter_path = "../resources/example_encounters.json"
        self.weapon_path = "../resources/example_weapons.json"
        self.food_path = "../resources/example_food.json"
        self.gas_path = "../resources/example_gas.json"
        self.materials_path = "../resources/example_materials.json"
        self.ammo_path = "../resources/example_ammo.json"

    def test_set_filename(self):
        """Test set filename method."""
        self.item_gen.set_member_file(self.encounter_path)

        assert self.item_gen.get_member_file() == self.encounter_path
        assert self.item_gen.get_members()['rare'][0]['title'] == "Puppy!"

    def test_item_generate(self):
        """Test generate method of ItemGenerator."""
        self.item_gen.set_member_file(self.weapon_path)
        example_weapons = ["Revolver", "Baseball Bat", "Hammer"]
        generated = self.item_gen.generate()

        assert generated['name'] in example_weapons

    def test_amount_generate(self):
        """Test generate method of AmountGenerator."""
        self.amount_gen.set_member_file(self.food_path)
        generated = self.amount_gen.generate()

        assert int(generated[0]) in range(0, 17)

    def test_item_amount_generate(self):
        """Test generate method of ItemAmountGenerator."""
        self.item_amount_gen.set_member_file(self.ammo_path)
        example_ammo = ["grenades", ".38", ".22"]
        generated = self.item_amount_gen.generate().split(" ")

        assert int(generated[0]) in range(0, 7)
        assert generated[1] in example_ammo


if __name__ == '__main__':
    unittest.main()
