#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sort_an_array' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def sort_an_array(n, arr):
    i = 0      # Pointer for the next 0
    curr = 0   # Current element being inspected
    j = n - 1  # Pointer for the next 2
    
    while curr <= j: # Only go until we hit the "2s" section
        if arr[curr] == 0:
            arr[curr], arr[i] = arr[i], arr[curr]
            i += 1
            curr += 1 # We can move curr because arr[i] was either 0 or 1
            
        elif arr[curr] == 2:
            arr[curr], arr[j] = arr[j], arr[curr]
            j -= 1
            # DO NOT increment curr here! 
            # We need to re-check the new value we just swapped from the back.
            
        else: # It's a 1
            curr += 1
            
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sort_an_array(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
