"""This module contains the logic behind the Zombie
Adventure application.
@author Kevin Hoopes
@version 7/2/2018
"""

###########
# IMPORTS #
###########

from random_generator import ItemGenerator, AmountGenerator, ItemAmountGenerator

####################
# CLASS DEFINITION #
####################

class ZombieApp():

    """An object to perform the application logic
    when requested.
    """

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

    def __init__(self):
        """Construct an instance of Zombie App."""
        self.weapon_gen = ItemGenerator(self.WEAPONS_PATH)
        self.in_enc_gen = ItemGenerator(self.IN_ENCOUNTERS_PATH)
        self.out_enc_gen = ItemGenerator(self.OUT_ENCOUNTERS_PATH)
        self.food_gen = AmountGenerator(self.FOOD_PATH)
        self.gas_gen = AmountGenerator(self.GAS_PATH)
        self.mater_gen = AmountGenerator(self.MATERIALS_PATH)
        self.ammo_gen = ItemAmountGenerator(self.AMMO_PATH)

    def generate_ammo(self):
        """Generate a random amount of ammo with a random type"""
        print(self.ammo_gen.generate())
