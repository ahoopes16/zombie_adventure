"""This is the main file which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

from pprint import pprint
from json_pipe import weapon_data, encounter_data

#############
# FUNCTIONS #
#############
def main():
    """
    Main function
    No params, no return
    """
    for weapon in weapon_data:
        pprint(weapon['name'])

    for encounter in encounter_data:
        pprint(encounter['name'])

main()
