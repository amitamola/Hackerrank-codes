'''
https://www.hackerrank.com/challenges/chocolate-feast/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    if n<c:
        return 0
    
    cho = n//c
    wrap = cho
    
    while True:
        if wrap//m>0:
            cho+=wrap//m
            wrap=wrap//m + wrap%m
        
        else:
            break
    return cho
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
