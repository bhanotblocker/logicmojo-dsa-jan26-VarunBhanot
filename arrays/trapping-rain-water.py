#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rain_water' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY hei as parameter.
#

def rain_water(height):
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    water = 0
    
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            water += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            
    return water
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    hei = list(map(int, input().rstrip().split()))

    result = rain_water(hei)

    fptr.write(str(result) + '\n')

    fptr.close()
