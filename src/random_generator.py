"""This class will load a JSON file and randomly generate
a member of that file when prompted based on a 'rarity'
field inside the members of the JSON file.
@author: Kevin Hoopes
@version: 6/28/2018"""

import json
import os
from pprint import pprint

class RandomGenerator:

    """Randomly generate members from a given file 
    when prompted.
    """

    def __init__(self):
        """Construct a default generator."""
        self._curr_dir = os.path.dirname(__file__)
        self._filename = ""
        self._members = []

    def __init__(self, filename):
        """Construct a generator with a filename.
        
        @param filename: the filename holding the members
        """
        self._curr_dir = os.path.dirname(__file__)
        self._filename = filename
        self._members = self._load_member_data()

    def _load_member_data(self):
        """Load the members to be randomly generated from
        the provided JSON file.
        """
        with open(os.path.join(self._curr_dir,
        	                   self._filename)) as mem_file:
            member_data = json.load(mem_file)

        return member_data

    def print_members(self):
        """Print the member data for sanity."""
        for member in self._members:
            pprint(member)
