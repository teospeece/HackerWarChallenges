#Teo Speece
#Instructions: The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
#
# Given a and b, determine their respective comparison points.

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    asum = 0
    bsum = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            asum += 1
        elif a[i] < b[i]:
            bsum += 1
        else:
            continue
    return asum, bsum