# =========================================================================================
# The file Advent_of_Code__2015__04.py was created by Johannes Macher
# @ Polymer Competence Center Leoben GmbH on the 2023-08-16
# =========================================================================================

# Task 04 - Part 1
"""
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is ckczppom.
"""

# Task 04 - Part 2
"""
Now find one that starts with six zeroes.
"""

# Imports
import hashlib


# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Generate HexCode for input
test_string = "ckczppom"
counter = 0
while True:
    current_string = test_string + str(counter)
    hexcode_result = hashlib.md5(current_string.encode("UTF-8")).hexdigest()

    if hexcode_result.startswith("00000"):
        print("\n")
        print("Lowest Number for Hash with leading 5 zeros: ", counter)
        break

    counter += 1

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
# Generate HexCode for input
counter = 0
while True:
    current_string = test_string + str(counter)
    hexcode_result = hashlib.md5(current_string.encode("UTF-8")).hexdigest()

    if hexcode_result.startswith("000000"):
        print("\n")
        print("Lowest Number for Hash with leading 6 zeros: ", counter)
        break

    counter += 1

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 & 2 solved by Narimiran
from hashlib import md5
from itertools import count


def solve(target, start=1):
    for i in count(start):
        m = md5(f"{INPUT}{i}".encode()).hexdigest()
        if m.startswith(target):
            return i


INPUT = "ckczppom"

print(solve(5 * "0"))
print(solve(6 * "0"))
