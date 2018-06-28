"""This is the main script which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

from encounter_generator import EncounterGenerator
from weapon_generator import WeaponGenerator

#############
# FUNCTIONS #
#############
def main():
    """
    Main function
    No params, no return
    """
    weapon_gen = WeaponGenerator()
    encounter_gen = EncounterGenerator()

    weapon_gen.print_weapons()
    encounter_gen.print_encounters()

main()
