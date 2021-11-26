#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    queries_size = len(queries)
    strings_size = len(strings)
    querie = 0
    string = 0
    results = [0] * queries_size
    while querie < queries_size:

        while string < strings_size:

            if queries[querie] == strings[string]:
                results[querie] = results[querie] + 1

            string = string + 1
        string = 0
        querie = querie + 1

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
