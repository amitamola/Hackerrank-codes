'''
https://www.hackerrank.com/challenges/alternating-characters/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    p = [False]
    for it in range(1, len(s)):
        if s[it]==s[it-1]:
            p.append(True)
            
        else:
            p.append(False)
            
    return sum(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
