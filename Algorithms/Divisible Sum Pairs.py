'''
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for val in list(combinations(range(len(ar)),2)):
        ind1, ind2 = val
        
        if (ar[ind1]+ar[ind2])%k==0:
            count+=1
        
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
