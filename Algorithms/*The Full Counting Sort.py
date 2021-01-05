'''
https://www.hackerrank.com/challenges/countingsort4/problem
'''

import math
import os
import random
import re
import sys

def countSort(arr):
    first_half = arr[:len(arr)//2]
    first_half_val = set([b for a,b in first_half])
        
    result = ['' for x in range(100)]
    
    for i, item in enumerate(arr):
        it, val = item
        
        if (val in first_half_val) and (i<len(arr)//2):
            result[int(it)] = result[int(it)]+' -'
        
        else:
            result[int(it)] = result[int(it)]+' '+val
            
    result = [x.strip() for x in result if len(x)>0]
    print(' '.join(result))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
