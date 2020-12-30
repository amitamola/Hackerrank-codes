'''
https://www.hackerrank.com/challenges/strong-password/problem
'''

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    count = 0
    
    if not bool(re.search(r'\d', password)):
        count+=1
    
    if not bool(re.search(r'[A-Z]', password)):
        count+=1
        
    if not bool(re.search(r'[a-z]', password)):
        count+=1
    
    if not bool(re.search(r'[!@#$%^&*()\-+]', password)):
        count+=1
        
    if len(password)+count<6:
        count+=6-len(password)-count
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
