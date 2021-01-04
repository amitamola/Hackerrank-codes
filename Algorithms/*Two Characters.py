'''
https://www.hackerrank.com/challenges/two-characters/problem
'''

import math
import os
import random
import re
import sys
from itertools import combinations

def isTwoAlter( s): 
    for i in range ( len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
          
    if (s[0] == s[1]): 
        return False
  
    return True


def alternate(s):
    valid = []
    for val in combinations(set(s), 2):
        string = ''.join([v for v in s if v in val])
        if isTwoAlter(string):
            valid.append(string)
        
    if len(valid)==0:
        return 0
    
    else:
        return max(map(len, valid))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
