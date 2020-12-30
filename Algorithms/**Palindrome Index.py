'''
https://www.hackerrank.com/challenges/palindrome-index/problem
'''

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def ifpalin(k):
    if k==k[::-1]:
        return True
    
    else:
        return False

def palindromeIndex(s):
    length = len(s)
    for val in range(length//2):
        rev = length- val-1
        if s[val]!=s[rev]:
            if ifpalin(s[val:rev]):
                return rev
            else:
                return val
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
