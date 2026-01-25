#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'find_missing' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_missing(arr):
    # Write your code here
    count = {}
    for ele in arr:
        count[ele] = count.get(ele,0)+1
        
    a = -1
    b = -1
    
    for i in range(1,len(arr)+1):
        if i not in count:
            b = i
        elif count[i]>=2:
            a=i
            
    
    return a,b
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = find_missing(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
