'''
https://www.hackerrank.com/challenges/quicksort1/problem
'''

import math
import os
import random
import re
import sys

def quickSort(arr):
    p = arr[0]
    
    first = []
    equal = [p,]
    last = []
    
    for val in arr[1:]:
        if val<p:
            first.append(val)
        
        elif val>p:
            last.append(val)
            
        else:
            equal.append(val)
    
    return first+equal+last

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
