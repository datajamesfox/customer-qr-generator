"""
Module to manage permutations of lists.
"""

import itertools
import random


class NamePermutations:
    """
    Generate unique names with no repeated elements up to a specified number.
    """

    def __init__(self, names, number):
        """
        Initialize with name list and list size.
        """
        self.names = names
        self.number = number

    def generate_permutations(self):
        """
        Generate unique pairs of names with no repeated elements.
        """
        return list(itertools.permutations(self.names, 2))

    def permutation_multiple(self):
        """
        Randomly generate n number of the existing permutations.
        """
        permutations = self.generate_permutations()
        n_permutation_list = random.choices(permutations, k=self.number)
        return (n_permutation_list)
