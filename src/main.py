"""This is the main script which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

from pprint import pprint
from random_generator import ItemGenerator

#############
# CONSTANTS #
#############

WEAPONS_PATH = "../resources/example_weapons.json"
ENCOUNTERS_PATH = "../resources/example_encounters.json"

#############
# FUNCTIONS #
#############

def main():
    """
    Host the game.
    """
    weapon_gen = ItemGenerator(WEAPONS_PATH)
    encounter_gen = ItemGenerator(ENCOUNTERS_PATH)

    pprint(weapon_gen.get_members())
    pprint(encounter_gen.get_members())
    pprint(weapon_gen.generate())

main()
