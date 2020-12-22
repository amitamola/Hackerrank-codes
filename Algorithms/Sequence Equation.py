'''
https://www.hackerrank.com/challenges/permutation-equation/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    k = []
    for it, val in enumerate(p):
        ind = p.index(it+1)+1
        k.append(p.index(ind)+1)
    return k
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
