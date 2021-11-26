#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    arr_size = len(a)
    x = 0
    y = 0
    isUnique = True
    while x < arr_size:

        while y < arr_size:

            if x == y:
                y = y + 1
                continue
            elif a[x] == a[y]:
                isUnique = False
                y = 0
                break
            y = y + 1
        if isUnique == True:
            return a[x]
        y = 0
        isUnique = True
        x = x + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
