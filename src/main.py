"""This is the main file which coordinates the zombie adventure
application.
@author: Kevin Hoopes
@version: 6/27/2018"""

import json
import os
from pprint import pprint

#############
# CONSTANTS #
#############
WEAPONS_FILE = "example_weapons.json"
ENCOUNTERS_FILE = "example_encounters.json"

#############
# FUNCTIONS #
#############
def main():
    """
    Main function
    No params, no return
    """
    curr_dir = os.path.dirname(__file__)
    weapons_path = "../resources/{}".format(WEAPONS_FILE)
    encounter_path = "../resources/{}".format(ENCOUNTERS_FILE)

    with open(os.path.join(curr_dir, weapons_path)) as w_file:
        weapon_data = json.load(w_file)

    with open(os.path.join(curr_dir, encounter_path)) as e_file:
        encounter_data = json.load(e_file)

    for weapon in weapon_data:
        pprint(weapon['name'])

    for encounter in encounter_data:
        pprint(encounter['name'])

main()
