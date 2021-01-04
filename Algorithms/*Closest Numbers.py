'''
https://www.hackerrank.com/challenges/closest-numbers/problem
'''

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    mini = 10000000000000
    
    keeper = []
    arr = sorted(arr)
    
    for i in range(len(arr)-1):
        summ = abs(arr[i]-arr[i+1])
        pair = (arr[i], arr[i+1])          
        
        if summ==mini:
            keeper.extend(pair)
            
        elif summ<mini:
            keeper = []
            keeper.extend(pair)
            mini = summ
            
        else:
            pass
    
    return keeper
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
