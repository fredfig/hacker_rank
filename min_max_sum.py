#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
# Calculate the sum of the array
    sum_arr = 0
    for number in arr:
        sum_arr = sum_arr + number
# Print the sum of the array without the max value for the minimal sum_arr
# Print the sum of the array without the min value for the maximal sum_arr
    print(sum_arr-max(arr), sum_arr-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
