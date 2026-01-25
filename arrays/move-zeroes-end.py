#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'move_func' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def move_func(n, arr):
    # Write your code here
    
    j = 0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = move_func(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()