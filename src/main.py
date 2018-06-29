"""This is the main script which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

from random_generator import RandomGenerator

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
    Main function
    No params, no return
    """
    weapon_gen = RandomGenerator(WEAPONS_PATH)
    encounter_gen = RandomGenerator(ENCOUNTERS_PATH)

    weapon_gen.print_members()
    encounter_gen.print_members()

main()
