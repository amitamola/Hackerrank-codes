'''
https://www.hackerrank.com/challenges/luck-balance/problem
'''

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    lucks, imp = zip(*contests)
    total_luck = sum(lucks)
    
    imp_contests= sum(imp)
    neg = 0
    
    contests = sorted(contests)
    
    only_imp = [k for k in contests if k[1]==1]
    
    if imp_contests<=k:
        return total_luck
    
    else:
        for a in range(imp_contests-k):
            neg+=only_imp[a][0]
        return total_luck-2*neg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
