# =========================================================================================
# The file Advent_of_Code__2015__02.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-16
# =========================================================================================

# Task 02
"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

"""

# Imports
import os
import numpy as np

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__01.txt")

santa_floor_string = str(np.loadtxt(load_path, delimiter=None, dtype=str))

# Calculate the number of string which puts Santa in the basement (-1)
santa_floor_list = list(santa_floor_string)

current_floor = 0
for idx, item in enumerate(santa_floor_list):
    if item == "(":
        current_floor += 1
    else:
        current_floor -= 1

    if current_floor == -1:
        break

# Print character which causes Santa to be in the basement (-1)
print(f"Character {(idx + 1):d} puts Santa in the basement.")
