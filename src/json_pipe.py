"""This file pulls weapon and encounter data from JSON
resources so that they may be easily imported by other
scripts.
@author: Kevin Hoopes
@version: 6/27/2018"""

import json
import os

#############
# CONSTANTS #
#############
CURR_DIR = os.path.dirname(__file__)
WEAPONS_PATH = "../resources/example_weapons.json"
ENCOUNTERS_PATH = "../resources/example_encounters.json"
WEAPON_DATA = []
ENCOUNTER_DATA = []

###############
# SCRIPT BODY #
###############
with open(os.path.join(CURR_DIR, WEAPONS_PATH)) as w_file:
    WEAPON_DATA = json.load(w_file)

with open(os.path.join(CURR_DIR, ENCOUNTERS_PATH)) as e_file:
    ENCOUNTER_DATA = json.load(e_file)
