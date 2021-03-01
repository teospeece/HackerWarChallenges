#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    print(ar)
    arlist = Counter(list(map(int, ar.split(','))))
    print('number',arlist[2])
    pairs = 0
    #index = 0
    for s in arlist:
        print(arlist[s]//2)
        pairs += arlist[s]//2
        #index += 1
    print('number of pairs', pairs)
    return pairs
    #print(pairs)
    #print(ar)
    #print(Counter(arlist))

    #sockcount = counter()
    #sockcount.update(ar)



sockMerchant(9,'10,20,20,10,10,30,50,10,20')
sockMerchant(10,'1,1,3,1,2,1,3,3,3,3')
