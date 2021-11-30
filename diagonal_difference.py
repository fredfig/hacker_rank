#!/bin/python3

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

    # Declaration of the diagonals and the size of the matrix
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)

    # Iterate on the matrix
    for i in range(0, n):

        left_diagonal += arr[i][i]
        right_diagonal += arr[i][n - i - 1]

    # Return of the absolute value of the diagonal difference sum
    return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
