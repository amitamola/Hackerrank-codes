'''
https://www.hackerrank.com/challenges/utopian-tree/problem
'''

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    start = 1
    
    for val in range(1, n+1):
        if val%2==0:
            start+=1
        
        else:
            start*=2
    return start
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
