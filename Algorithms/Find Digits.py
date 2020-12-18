'''
https://www.hackerrank.com/challenges/find-digits/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    nums = tuple(map(int, list(str(n))))
    
    count = 0
    
    for val in nums:
        if val==0:
            continue
        
        elif n%val==0:
            count+=1
            
        else:
            continue
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
