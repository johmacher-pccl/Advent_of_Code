# =========================================================================================
# The file Advent_of_Code__2015__06.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-17
# =========================================================================================

# Task 07 - Part 1
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

# Task 07 - Part 2
"""
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

# Imports
import os
from functools import lru_cache
from operator import and_, or_, lshift, rshift

# read in string from data
home_directory = os.path.dirname(__file__)
load_path = os.path.join(home_directory, "Data_2015", "Data__Advent_of_Code__2015__07.txt")

data = open(load_path).read().splitlines()


# ----------------------------------------------------------------------------------------------------------------------
# (Mostly by Narimiran)
# find wire a
# Make input into into dictionary
parse_input = lambda data: {(s := line.split(" -> "))[1]: s[0].split() for line in data}
wires = parse_input(data)


def get_value(wires, wire="a", b=None):
    # Directory for aligning commands in input with operations
    operations = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}

    # Decorator to memorize former executions of the function: allowing something like recursive handling of the input data (no solution possible without)
    @lru_cache
    def aux(wire):  # Auxiliary nested function trying if value can be assigned otherwise recursion
        try:
            # value can be assigned
            return int(wire)
        except ValueError:
            # commands are read out and are processed in return
            lhs = wires[wire]
        return (
            aux(lhs[0])
            if len(lhs) == 1
            else ~aux(lhs[1]) & 0xFFFF
            if len(lhs) == 2
            else operations[lhs[1]](aux(lhs[0]), aux(lhs[2]))
        )
        # 1st two lines of return: Simple assignment to value, 2nd two Lines: bitwise not as complement to the 16bit maximum value, last line: execution of operators

    # b assignment for second part
    if b is not None:
        wires["b"] = [b]
    return aux(wire)


# Part 1
print("\n")
print("Wire 'a' is: ", first := get_value(wires))
print("With new 'b' wire 'a' is now: ", get_value(wires, b=first))
print("\n")
