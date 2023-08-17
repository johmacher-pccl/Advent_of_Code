# =========================================================================================
# The file Advent_of_Code__2015__03.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-16
# =========================================================================================

# Task 03 - Part 1
"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole
calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^),
south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

# Task 03 - Part 2
"""
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving
based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""

# Imports
import os
import numpy as np
import copy
import matplotlib.pyplot as plt

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__03.txt")

direction_string = str(np.loadtxt(load_path, delimiter=None, dtype=str))


# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Calculate the number of houses visited once
house_map = np.array([[1]])

x_index = 0
y_index = 0

for direction in direction_string:
    # North
    if direction == "^":
        y_index -= 1
        if y_index < 0:
            # Resize house map
            array_add_on = np.zeros((1, house_map.shape[1]))
            house_map = np.concatenate((array_add_on, house_map), axis=0)
            y_index = 0

    # South
    elif direction == "v":
        y_index += 1
        if y_index > house_map.shape[0] - 1:
            array_add_on = np.zeros((1, house_map.shape[1]))
            house_map = np.concatenate((house_map, array_add_on), axis=0)

    # West
    elif direction == "<":
        x_index -= 1
        if x_index < 0:
            # Resize house map
            array_add_on = np.zeros((house_map.shape[0], 1))
            house_map = np.concatenate((array_add_on, house_map), axis=1)
            x_index = 0

    # East
    else:
        x_index += 1
        if x_index > house_map.shape[1] - 1:
            array_add_on = np.zeros((house_map.shape[0], 1))
            house_map = np.concatenate((house_map, array_add_on), axis=1)

    # Add present
    house_map[y_index, x_index] += 1

# Calculate how many houses got at least one presen
number_of_house_with_presents = np.sum(house_map > 0)
print("\n")
print(f"Number of houses with at least one present: {number_of_house_with_presents:.0f}")

plt.figure()
img = plt.imshow(house_map)
img.set_cmap("hot")
plt.axis("off")

# ----------------------------------------------------------------------------------------------------------------------
# Part Two calculate Houses with Robo-Santa
house_map = np.array([[2]])

x_index_santa = 0
y_index_santa = 0

x_index_robo = 0
y_index_robo = 0

for idx, direction in enumerate(direction_string):
    x_offset = 0
    y_offset = 0

    if idx % 2 == 0:
        bool_santa = True
        x_dummy = copy.copy(x_index_santa)
        y_dummy = copy.copy(y_index_santa)

    else:
        bool_santa = False
        x_dummy = copy.copy(x_index_robo)
        y_dummy = copy.copy(y_index_robo)

    # North
    if direction == "^":
        y_dummy -= 1
        if y_dummy < 0:
            # Resize house map
            array_add_on = np.zeros((1, house_map.shape[1]))
            house_map = np.concatenate((array_add_on, house_map), axis=0)
            y_dummy = 0
            y_offset = 1

    # South
    elif direction == "v":
        y_dummy += 1
        if y_dummy > house_map.shape[0] - 1:
            array_add_on = np.zeros((1, house_map.shape[1]))
            house_map = np.concatenate((house_map, array_add_on), axis=0)

    # West
    elif direction == "<":
        x_dummy -= 1
        if x_dummy < 0:
            # Resize house map
            array_add_on = np.zeros((house_map.shape[0], 1))
            house_map = np.concatenate((array_add_on, house_map), axis=1)
            x_dummy = 0
            x_offset = 1

    # East
    else:
        x_dummy += 1
        if x_dummy > house_map.shape[1] - 1:
            array_add_on = np.zeros((house_map.shape[0], 1))
            house_map = np.concatenate((house_map, array_add_on), axis=1)

    # Add present
    house_map[y_dummy, x_dummy] += 1

    if bool_santa:
        x_index_santa = copy.copy(x_dummy)
        y_index_santa = copy.copy(y_dummy)

        x_index_robo += x_offset
        y_index_robo += y_offset

    else:
        x_index_robo = copy.copy(x_dummy)
        y_index_robo = copy.copy(y_dummy)

        x_index_santa += x_offset
        y_index_santa += y_offset

# Calculate how many houses got at least one presen
number_of_house_with_presents = np.sum(house_map > 0)
print(f"Number of houses with at least one present (Santa & Robo-Santa): {number_of_house_with_presents:.0f}")
print("\n")

plt.figure()
img = plt.imshow(house_map)
img.set_cmap("hot")
plt.axis("off")

plt.show(block=False)


# ----------------------------------------------------------------------------------------------------------------------
# Part 1 & 2 solved by Narimiran
def solve(data, players=1):
    directions = {"^": -1j, "v": +1j, "<": -1, ">": 1}
    locations = [0] * players
    visited = {0}
    for i, d in enumerate(data):
        locations[i % players] += directions[d]
        visited |= {locations[i % players]}

    print(locations)
    print(visited)
    return len(visited)


data = open(load_path).readline()

print(solve(data))
print(solve(data, 2))
