'''
https://www.hackerrank.com/challenges/picking-numbers/problem
'''

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    kl = []
    j = []
    a.sort()
        
    for val in a:
        if len(j)==0:
            j.append(val)
            continue
        
        elif abs(min(j)-val)<=1:
            j.append(val)
            
        else:
            kl.append(j)
            j=[val,]
    
    kl.append(j)
            
    return max(map(len, kl))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
