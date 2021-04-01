#!/bin/python3
#Teo Speece
#Instructions: Given a square matrix, calculate the absolute difference between the sums of its diagonals.


import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    print(arr)
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
    #    print(arr[i][i])
        d1 += arr[i][i]
    for j in range(len(arr)):
        d2 += arr[j][len(arr)-j-1]
    # print(d1)
    # print(d2)
    return abs(d1 -d2)