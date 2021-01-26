'''
https://www.hackerrank.com/challenges/mark-and-toys/problem
'''

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    prices= sorted(prices)
    summ = 0
    count = 0
    
    if k<prices[0]:
        return 0
    
    else:
        while summ<=k:
            summ+=prices[count]
            count+=1
    
    return count-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
