"""This class will randomly generate an encounter when prompted.
@author: Kevin Hoopes
@version: 6/27/2018"""

from pprint import pprint
from json_pipe import ENCOUNTER_DATA

class EncounterGenerator:
    """Object to randomly generate encounters
    when prompted"""
    def __init__(self):
        """Default constructor"""
        self.encounter_data = ENCOUNTER_DATA

    def print_encounters(self):
        """Print the encounter data for sanity"""
        for encounter in self.encounter_data:
            pprint(encounter)
