#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
# 5
# 1 2 1 3 2
# 3 2
# 2
# d = 3 = soma
# m = 2 = itens consecutivos

def birthday(s, d, m):
    n = len(s)
    num_ways = 0
    sum_temp = 0
    x = 0
    i = 0
    while i < n:
        while x < m:
            if x+i < n:
                sum_temp += s[x+i]
            x += 1
        if sum_temp == d:
            num_ways += 1
        x = 0
        sum_temp = 0
        i += 1

    return num_ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
