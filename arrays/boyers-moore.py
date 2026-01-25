#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'majorityElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def majorityElement(n, arr):
    # Write your code here
    king = None
    strength = 0
    for person in arr:
        if strength == 0:
            king = person
            strength = 1
        elif person == king:
            strength += 1
        else:
            strength -= 1
            
    count = 0
    for person in arr:
        if person == king:
            count += 1
            
    if count > len(arr) // 2:
        return king
    else:
        return -1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = majorityElement(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
