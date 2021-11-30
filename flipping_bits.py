#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):

    # Transform the integer in a binary string only with numbers
    binary_string = bin(n)[2 : ]

    # Create a list with the rest of the binary format of the integer
    binary_list = ['0'] * (32 - len(binary_string))

    # Include the binary number in que list
    for x in binary_string:
        binary_list.append(x)

    # Declaration of the inverse String
    binary_inverse = ''

    # Iteration for the flipping bits saving on the string
    for i in binary_list:
        if i == '0':
            binary_inverse += '1'
        else:
            binary_inverse += '0'

    # Convert the binary inverse in a integer
    inteiro = int(binary_inverse, 2)

    return inteiro

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
