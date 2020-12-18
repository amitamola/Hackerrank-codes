'''
https://www.hackerrank.com/challenges/between-two-sets/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Write your code here
    all_useful = []
    
    if a[-1]>b[0]:
        return 0
    
    for val in range(a[-1], b[0]+1):
        p = list(map(lambda x:val%x==0, a))
        q = list(map(lambda x:x%val==0, b))
        
        if all(p) and all(q):
            all_useful.append(val)
            
    return len(all_useful)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
