'''
https://www.hackerrank.com/challenges/repeated-string/problem
'''

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    length = len(s)
    if n<=length:
        return s[:n].count('a')
    
    elif n%length==0:
        return s.count('a')*(n//len(s))
        
    else:
        first = s.count('a')*(n//len(s))
        second = s[:n%len(s)].count('a')
        
        return (first+second)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
