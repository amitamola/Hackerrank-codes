'''
https://www.hackerrank.com/challenges/anagram/problem
'''

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    if len(s)%2==1:
        return -1
    
    else:
        half = len(s)//2
        a = s[:half]
        b = s[half:]
        
        if a==b:
            return 0
        
        else:
            return len(a)-len(tuple((Counter(a) & Counter(b)).elements()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
