"""This module contains a testing suite for the Random
Generator class.
@author: Kevin Hoopes
@version: 7/1/2018
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath('..'))
from src.random_generator import RandomGenerator

class GeneratorTests(unittest.TestCase):

    """Hold the test cases for the Random Generator
    class."""

    def setUp(self):
        """Set up variables to run tests against."""
        self.generator = RandomGenerator()
        self.encounter_path = "../resources/example_encounters.json"
        self.weapon_path = "../resources/example_weapons.json"
        self.generator.set_member_file(self.encounter_path)

    def test_set_filename(self):
        """Test set filename method."""
        assert self.generator.get_member_file() == self.encounter_path
        assert self.generator.get_members()['rare'][0]['title'] == "Puppy!"

    def test_generate(self):
        """Test determine rarity method."""

        self.generator.set_member_file(self.weapon_path)
        generated = self.generator.generate()
        example_weapons = ["Revolver", "Baseball Bat", "Hammer"]
        assert generated['name'] in example_weapons

if __name__ == '__main__':
    unittest.main()
