#Teo Speece
#Instructions: Given the sequence of up and down steps during a hike,
# find and print the number of valleys walked through.
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    path = path
    valley = 0
    current = 0
    for i in range(len(path)):
        print(current)
        if current == 0 and path[i] == 'D':
            valley += 1
        if path[i] == 'U':
            current += 1
        else:
            current -= 1
    print("number of valleys", valley)
    return valley



countingValleys(8,['U','D','D','D','U','D','U','U'])