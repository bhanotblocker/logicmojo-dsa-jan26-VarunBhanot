#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER target
#  2. INTEGER n
#  3. INTEGER_ARRAY arr
#

def twoSum(target, n, arr):
    i = 0
    j = len(arr)-1
    
    while i < j:
        if arr[i]+arr[j]==target:
            return i+1,j+1
        elif arr[i]+arr[j]<target:
            i+=1
        elif arr[i]+arr[j]>target:
            j-=1
    
    return None
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    targert = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = twoSum(targert, n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
