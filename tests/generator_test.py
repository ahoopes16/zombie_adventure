"""This module contains a testing suite for the Random
Generator class.
@author: Kevin Hoopes
@version: 7/2/2018
"""

###########
# IMPORTS #
###########

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath('..'))
from src.random_generator import ItemGenerator, AmountGenerator, ItemAmountGenerator

##############
# TEST SUITE #
##############

class GeneratorTests(unittest.TestCase):

    """Hold the test cases for the Random Generator
    class."""

    #############
    # CONSTANTS #
    #############

    WEAPONS_PATH = "../sample_resources/example_weapons.json"
    IN_ENCOUNTERS_PATH = "../sample_resources/example_in_encounters.json"
    OUT_ENCOUNTERS_PATH = "../sample_resources/example_out_encounters.json"
    FOOD_PATH = "../sample_resources/example_food.json"
    GAS_PATH = "../sample_resources/example_gas.json"
    MATERIALS_PATH = "../sample_resources/example_materials.json"
    AMMO_PATH = "../sample_resources/example_ammo.json"

    #############
    # FUNCTIONS #
    #############

    def setUp(self):
        """Set up variables to run tests against."""
        self.item_gen = ItemGenerator()
        self.amount_gen = AmountGenerator()
        self.item_amount_gen = ItemAmountGenerator()

    def test_set_filename(self):
        """Test set filename method."""
        self.item_gen.set_member_file(self.OUT_ENCOUNTERS_PATH)

        assert self.item_gen.get_member_file() == self.OUT_ENCOUNTERS_PATH
        assert self.item_gen.get_members()['rare'][0]['title'] == "Puppy!"

    def test_item_generate(self):
        """Test generate method of ItemGenerator."""
        self.item_gen.set_member_file(self.WEAPONS_PATH)
        example_weapons = ["Revolver", "Baseball Bat", "Hammer"]
        generated = self.item_gen.generate()

        assert generated['name'] in example_weapons

    def test_amount_generate(self):
        """Test generate method of AmountGenerator."""
        self.amount_gen.set_member_file(self.FOOD_PATH)
        generated = self.amount_gen.generate()

        assert int(generated[0]) in range(0, 17)

    def test_item_amount_generate(self):
        """Test generate method of ItemAmountGenerator."""
        self.item_amount_gen.set_member_file(self.AMMO_PATH)
        example_ammo = ["grenades", ".38", ".22"]
        generated = self.item_amount_gen.generate().split(" ")

        assert int(generated[0]) in range(0, 7)
        assert generated[1] in example_ammo


if __name__ == '__main__':
    unittest.main()
