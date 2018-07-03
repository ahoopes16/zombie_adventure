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
    app.generate_ammo()

main()
