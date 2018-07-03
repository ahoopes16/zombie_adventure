"""This is the main script which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 7/2/2018
"""

###########
# IMPORTS #
###########

from zombie_app import ZombieApp

#############
# FUNCTIONS #
#############

def main():
    """
    Host the game.
    """
    app = ZombieApp()
    app.generate_weapon()
    app.generate_encounter("inside")
    app.generate_encounter("outside")
    app.generate_food()
    app.generate_gas()
    app.generate_materials()
    app.generate_ammo()

main()
