'''
https://www.hackerrank.com/challenges/beautiful-binary-string/problem
'''

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
    i = 0
    count = 0
    while True:
        if "010" in b[i:]:
            i = b.find('010', i)+3
            count+=1
            
        else:
            break
    
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
