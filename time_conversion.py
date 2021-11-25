#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0]+s[1])
    AM_PM = s[8]+s[9]
    if hour == 12:
        if AM_PM == 'PM':
            return s[0:8]
        else:
            return '00'+s[2:8]
    elif AM_PM == 'AM':
        return s[0:8]
    elif AM_PM == 'PM':
        return str(hour+12)+s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
