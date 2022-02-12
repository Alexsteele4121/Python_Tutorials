# PART 29: The Binary Search Algorithm (Activity)

# Binary search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing in half the portion of the list that could contain the item,
# until you've narrowed down the possible locations to just one.

# Imports
from random import randint


# Global Variables
dataset = set(randint(0, 1000) for _ in range(100))
dataset = sorted(dataset)
print(*dataset)


# Functions
