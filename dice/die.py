"""Class for create dice objects."""
from random import randint


class Die():
    """"A class representing a single die."""

    def __init__(self, num_sides=6):
        """Create die. Six sided die is the default."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
