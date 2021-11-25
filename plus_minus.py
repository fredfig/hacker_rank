#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zer_count = 0
    tot_count = 0
    for number in arr:
        if number > 0:
            pos_count = pos_count + 1
            continue
        elif number < 0:
            neg_count = neg_count + 1
            continue
        else:
            zer_count = zer_count + 1
    tot_count = pos_count + neg_count + zer_count
    print("{:.6f}".format(pos_count/tot_count))
    print("{:.6f}".format(neg_count/tot_count))
    print("{:.6f}".format(zer_count/tot_count))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
