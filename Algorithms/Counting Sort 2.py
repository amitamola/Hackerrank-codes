'''
https://www.hackerrank.com/challenges/countingsort2/problem
'''

import math
import os
import random
import re
import sys

def countingSort(arr):
    result = [0]*100
    
    for val in arr:
        result[val]+=1
    
    final = []
    
    for it, val in enumerate(result):
        if val==0:
            pass
        
        else:
            final.extend([it]*val)
            
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
