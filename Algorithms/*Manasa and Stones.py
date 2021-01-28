'''
https://www.hackerrank.com/challenges/manasa-and-stones/problem
'''

import math
import os
import random
import re
import sys

def stones(n, a, b):
    ans = set()
    for i in range(n):
        c = b*i + a*(n-i-1)
        ans.add(c)
        
    return sorted(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
