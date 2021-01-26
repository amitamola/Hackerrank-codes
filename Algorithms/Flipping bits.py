'''
https://www.hackerrank.com/challenges/flipping-bits/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    val = bin(n).split('b')[1]
    val = '0'*(32-len(val)) + val
    
    new = ''
    
    for v in val:
        if v=='0':
            new+='1'
        else:
            new+='0'
    
    return int(new, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
