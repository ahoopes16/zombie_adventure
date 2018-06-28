"""This class will randomly generate a weapon when prompted.
@author: Kevin Hoopes
@version: 6/27/2018"""

from pprint import pprint
from json_pipe import WEAPON_DATA

class WeaponGenerator:
    """Object to randomly generate encounters
    when prompted"""
    def __init__(self):
        """Default constructor"""
        self.weapon_data = WEAPON_DATA

    def print_weapons(self):
        """Print the weapon data for sanity"""
        for weapon in self.weapon_data:
            pprint(weapon)
