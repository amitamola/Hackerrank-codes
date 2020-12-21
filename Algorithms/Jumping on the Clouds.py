'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # 0 0 0 1 0 0 
    it = 0
    jump = 0
    while it<len(c)-1:
        if (it+1==len(c)-1) or (it+2==len(c)-1):
            jump+=1
            return jump
        
        elif (c[it+2]==1) or (it+1>=len(c)-2):
            it+=1
            
        else:
            it+=2
            
        jump+=1
        
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
