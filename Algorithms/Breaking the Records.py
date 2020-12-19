'''
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    hi = scores[0]
    lo = scores[0]
    hi_co = 0
    lo_co = 0
    
    for val in scores[1:]:
        if val>hi:
            hi=val
            hi_co+=1
        
        elif val<lo:
            lo = val
            lo_co+=1
    return(hi_co, lo_co) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
