import sys, os, pytest
sys.path.insert(0, os.path.abspath('..'))
from src.random_generator import RandomGenerator

def test_set_filename():
    generator = RandomGenerator()
    ENCOUNTER_PATH = "../resources/example_encounters.json"
    generator.set_member_file(ENCOUNTER_PATH)
    assert generator.get_member_file() == ENCOUNTER_PATH
    assert generator.get_members()[0]['title'] == "Puppy!"