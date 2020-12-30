'''
https://www.hackerrank.com/challenges/reduced-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    while True:
        l = [m.group(0) for m in re.finditer('(\w)\\1?',s)]
        
        if len(s)==0:
            return 'Empty String'
        
        elif len(l)==len(s):
            return s
        
        else:
            j = [x for x in l if len(x)<2]
            s = ''.join(j)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
