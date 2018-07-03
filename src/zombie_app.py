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

    WEAPONS_PATH = "../resources/weapons.json"
    IN_ENCOUNTERS_PATH = "../resources/in_encounters.json"
    OUT_ENCOUNTERS_PATH = "../resources/out_encounters.json"
    FOOD_PATH = "../resources/food.json"
    GAS_PATH = "../resources/gas.json"
    MATERIALS_PATH = "../resources/materials.json"
    AMMO_PATH = "../resources/ammo.json"

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

    def generate_weapon(self):
        """Generate a random weapon."""
        weapon = self.weapon_gen.generate()

        if weapon['ammo'] == 'none':
            print("You found a {}! It does {} damage!".format(weapon['name'],
                                                              weapon['damage']))
        else:
            print("You found a {}! It does {} damage and uses {}!".format(weapon['name'],
                                                                          weapon['damage'],
                                                                          weapon['ammo']))

    def generate_encounter(self, location):
        """Generate an encounter for a specific location.

        @param location: the location of the encounter
        """
        if location == "inside":
            encounter = self.in_enc_gen.generate()
        else:
            encounter = self.out_enc_gen.generate()

        print(encounter['title'])
        print("===================")
        print(encounter['details'])

    def generate_food(self):
        """Generate a random amount of food."""
        print(self.food_gen.generate())

    def generate_gas(self):
        """Generate a random amount of gas."""
        print(self.gas_gen.generate())

    def generate_materials(self):
        """Generate a random amount of materials."""
        print(self.mater_gen.generate())

    def generate_ammo(self):
        """Generate a random amount of ammo
        with a random type."""
        print(self.ammo_gen.generate())
