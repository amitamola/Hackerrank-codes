'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    re = Counter(s)
    sec = Counter(re.values())
    
    keys = tuple(sec.keys())
    
    if len(sec)>2:
        return "NO"
    
    elif len(sec)==1:
        return "YES"
    
    else:
        if 1 in sec and sec[1]==1:
            return "YES"
        
        elif (abs(keys[0]-keys[1])==1) and (1 in sec.values()):
            return "YES"
        
        else:
            return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
