"""This is the main file which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

from pprint import pprint
from json_pipe import WEAPON_DATA, ENCOUNTER_DATA

#############
# FUNCTIONS #
#############
def main():
    """
    Main function
    No params, no return
    """
    for weapon in WEAPON_DATA:
        pprint(weapon)

    for encounter in ENCOUNTER_DATA:
        pprint(encounter)

main()
