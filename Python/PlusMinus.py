#Teo Speece
#Instructions: Given an array of integers, calculate the ratios of its elements that are positive,
# negative, and zero. Print the decimal value of each fraction on a new line with  places after
# the decimal.
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] == 0:
            zer += 1
        else:
            neg += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))