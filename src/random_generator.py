"""This class will load a JSON file and randomly generate
a member of that file when prompted based on a 'rarity'
field inside the members of the JSON file.
@author: Kevin Hoopes
@version: 6/28/2018"""

import json
import os
from numpy.random import choice

class RandomGenerator:

    """Randomly generate members from a given file
    when prompted.
    """

    def __init__(self, filename=""):
        """Construct a generator with a filename.

        @param filename: the filename holding the members
        """
        self._curr_dir = os.path.dirname(__file__)
        self._member_file = filename
        self._members = []

        self.rare = 0.1
        self.uncommon = 0.2
        self.common = 0.7

        if self._member_file != "":
            self._load_member_data()

    def _load_member_data(self):
        """Load the members to be randomly generated from
        the provided JSON file.
        """
        try:
            mem_file = open(os.path.join(self._curr_dir,
                                         self._member_file))
            self._members = json.load(mem_file)
            mem_file.close()

        except IOError as err:
            print("Couldn't read file {}.\nReceived error: {}.\n\
            	  ".format(self._member_file, err.strerror))

    def _determine_rarity(self):
        """Determine the rarity of the member to be
        returned.
        """
        rarities = ["rare", "uncommon", "common"]
        weights = [self.rare, self.uncommon, self.common]

        return choice(rarities, p=weights)

    def set_member_file(self, filename):
        """Set the generator's member file and reload
        the JSON data.

        @param filename: the new JSON file to be opened
        """
        if self._member_file != filename:
            self._member_file = filename
            self._load_member_data()

    def get_member_file(self):
        """Return the generator's member file."""
        return self._member_file

    def get_members(self):
        """Return the generator's member data."""
        return self._members

    def generate(self):
        """Return a random member for use."""
        chosen_rarity = self._determine_rarity()
        return choice(self._members[chosen_rarity])
