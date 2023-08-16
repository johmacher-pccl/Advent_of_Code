# =========================================================================================
# The file Advent_of_Code__2015__01.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-16
# =========================================================================================

# Task 01
"""
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

"""

# Imports
import os
import numpy as np

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__01.txt")

santa_floor_string = str(np.loadtxt(load_path, delimiter=None, dtype=str))

# Count characters
floor_number = santa_floor_string.count("(") - santa_floor_string.count(")")

# Print Floor
print("Floor Number: ", floor_number)
