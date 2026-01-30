#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER n
#

def maxProfit(a, n):
    total_profit = 0
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            total_profit += a[i] - a[i-1]
            
    return total_profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    profit = maxProfit(price, n)

    fptr.write(str(profit) + '\n')

    fptr.close()
