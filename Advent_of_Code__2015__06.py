# =========================================================================================
# The file Advent_of_Code__2015__06.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-17
# =========================================================================================

# Task 06 - Part 1
"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""

# Task 06 - Part 2
"""

"""

# Imports
import os
import numpy as np

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__06.txt")

data = open(load_path).read().splitlines()


# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Count ligths
def parse_line(line):
    words = line.split()  # since only whitespaces are split
    x1, y1 = map(int, words[-3].split(","))  # since from back is always the same
    x2, y2 = map(int, words[-1].split(","))  # since from back is always the same
    return (
        words[len(words) == 5],
        x1,
        x2,
        y1,
        y2,
    )  # with 5 words the second word (since -->1), with 4 words (toggel) the first word (since --> 0)


# Read data to switch out lights
def switch_lights(data_in, light_map_in):
    for cmd, x1, x2, y1, y2 in data_in:
        if cmd == "on":
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] = 1

        elif cmd == "off":
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] = 0

        else:
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] = np.logical_not(light_map_in[y1 : y2 + 1, x1 : x2 + 1]).astype(int)

    return light_map_in


# solve Part 1: Count lights
light_map = np.zeros((1000, 1000))
light_map = switch_lights(map(parse_line, data), light_map)
print("\n")
print(f"Part 1: Lights switched on: {np.sum(light_map):.0f}")

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Count brightness
# Read data to switch out lights
light_map = np.zeros((1000, 1000))


def switch_brightness(data_in, light_map_in):
    for cmd, x1, x2, y1, y2 in data_in:
        if cmd == "on":
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] += 1

        elif cmd == "off":
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] -= 1
            light_map_in = np.maximum(light_map_in, 0)

        else:
            light_map_in[y1 : y2 + 1, x1 : x2 + 1] += 2

    return light_map_in


light_map = np.zeros((1000, 1000))
light_map = switch_brightness(map(parse_line, data), light_map)
print(f"Part 1: Measured brightness: {np.sum(light_map):.0f}")
print("\n")
