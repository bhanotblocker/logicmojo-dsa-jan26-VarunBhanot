#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'first_missing_positive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def first_missing_positive(n, nums):
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
            
    # 2. Mark existing numbers by flipping signs
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            idx = val - 1
            if nums[idx] > 0: 
                nums[idx] = -nums[idx]
                
    # 3. Find the first positive index
    for i in range(n):
        if nums[i] > 0:
            return i + 1
            
    return n + 1
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = first_missing_positive(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
