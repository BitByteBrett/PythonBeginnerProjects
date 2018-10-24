#!/usr/bin/env python3
"""Print out lyrics to 99 Bottles of Beer On The Wall

Usage:

    python3 99bottles.py
"""

bottles_list = list(reversed(range(100)))

for i in bottles_list:
    if i > 1:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
        if i > 2:
            print("Take one down and pass it around, {0} bottles of beer on the wall.\n".format(i-1))
        if i == 2:
            print("Take one down and pass it around, {0} bottle of beer on the wall.\n".format(i-1))
    if i == 1:
        print("{0} bottle of beer on the wall, {0} bottle of beer.\n"
              "Take one down and pass it around, no more bottles of beer on the wall.\n".format(i))
    if i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.\n"
              "Go to the store and buy some more, {0} bottles of beer on the wall.".format(bottles_list.index(0)))
