#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'left_right' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def left_right(arr):
    
    minarr = [0]*len(arr)
    
    minarr[-1] = arr[-1]
    
    for i in range (n-2,-1,-1):
            minarr[i] = min(arr[i],minarr[i+1])
            
    maxleft = arr[0]
    
    for i in range(1,n-1):
        
        if maxleft<=arr[i]<=minarr[i+1]:
            return arr[i]
        if arr[i]>maxleft:
            maxleft = arr[i]
            
            
    return -1
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = left_right(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
