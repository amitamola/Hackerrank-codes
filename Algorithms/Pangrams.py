'''
https://www.hackerrank.com/challenges/pangrams/problem
'''

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    k = set(s.lower())
    
    for val in [' ', '.', ',', ':']:
        if val in k:
            k.remove(val)
            
    if len(k)==26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
