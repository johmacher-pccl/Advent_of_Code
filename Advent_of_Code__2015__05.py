# =========================================================================================
# The file Advent_of_Code__2015__05.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-16
# =========================================================================================

# Task 05 - Part 1
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

# Task 05 - Part 2
"""
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""

# Imports
import os
import re
import numpy as np

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__05.txt")

naughty_and_good_strings = np.loadtxt(load_path, delimiter=None, dtype=str)

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Count characters
vowels = "aeiou"

nice_counter = 0
for string in naughty_and_good_strings:
    # Number of vowels
    vowel_count = len([char for char in string if char in "aeiou"])

    # Double letters
    bool_double = False
    for idx in range(len(string) - 1):
        if string[idx] == string[idx + 1]:
            bool_double = True
            break

    # Naughty strings
    stringA = "ab"
    stringB = "cd"
    stringC = "pq"
    stringD = "xy"
    pattern = re.compile(r"{}|{}|{}|{}".format(stringA, stringB, stringC, stringD))
    bool_found = pattern.search(string)

    if vowel_count >= 3 and bool_double and not bool(bool_found):
        nice_counter += 1

print("\n")
print("Number of nice strings: ", nice_counter)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
p = re.compile(r"\b(\w+)\s+\1\b")
