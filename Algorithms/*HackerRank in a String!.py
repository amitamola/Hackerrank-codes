'''
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    string_length = len(s)
    
    k = 0
    p = 0
    desired = 'hackerrank'
    final = ''
    
    while k<string_length:
        if s[k]==desired[p]:
            p+=1
            final+=s[k]
            
        if final==desired:
            return 'YES'
        
        k+=1

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
