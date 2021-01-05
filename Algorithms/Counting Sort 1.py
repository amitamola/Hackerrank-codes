'''
https://www.hackerrank.com/challenges/countingsort1/problem
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
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
