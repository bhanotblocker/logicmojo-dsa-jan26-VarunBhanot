#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'max_consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def max_consecutive(a):
    
    one_so_far = 0
    max_ones = 0

    for i in range(len(a)):
            if a[i]==1:
                    one_so_far +=1


            if one_so_far> max_ones:
                    max_ones = one_so_far


            if a[i] == 0:
                    one_so_far = 0
                    
    return max_ones
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = max_consecutive(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
