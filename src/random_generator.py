"""This class will load a JSON file and randomly generate
a member of that file when prompted based on a 'rarity'
field inside the members of the JSON file.
@author: Kevin Hoopes
@version: 6/28/2018"""

import json
import os

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
