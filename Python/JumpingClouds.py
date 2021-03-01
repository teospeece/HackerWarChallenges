#Teo Speece
#Instructions: Determine the minimum number of jumps it will take to jump from the starting postion
# to the last cloud. It is always possible to win the game.

#For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0
    moves = 0
    while current < len(c) - 1:
        if current + 2 < len(c) and c[current +2] != 1:
            current += 1
        current += 1
        moves += 1
    return moves

