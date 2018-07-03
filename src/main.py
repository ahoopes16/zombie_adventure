"""This is the main script which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 7/2/2018
"""

###########
# IMPORTS #
###########

from pprint import pprint
from random_generator import ItemGenerator, AmountGenerator, ItemAmountGenerator

#############
# CONSTANTS #
#############

WEAPONS_PATH = "../sample_resources/example_weapons.json"
ENCOUNTERS_PATH = "../sample_resources/example_encounters.json"
FOOD_PATH = "../sample_resources/example_food.json"
GAS_PATH = "../sample_resources/example_gas.json"
MATERIALS_PATH = "../sample_resources/example_materials.json"
AMMO_PATH = "../sample_resources/example_ammo.json"

#############
# FUNCTIONS #
#############

def main():
    """
    Host the game.
    """
    weapon_gen = ItemGenerator(WEAPONS_PATH)
    food_gen = AmountGenerator(FOOD_PATH)
    gas_gen = AmountGenerator(GAS_PATH)
    materials_gen = AmountGenerator(MATERIALS_PATH)
    ammo_gen = ItemAmountGenerator(AMMO_PATH)


    pprint(weapon_gen.generate())
    pprint(food_gen.generate())
    pprint(gas_gen.generate())
    pprint(materials_gen.generate())
    pprint(ammo_gen.generate())

main()
