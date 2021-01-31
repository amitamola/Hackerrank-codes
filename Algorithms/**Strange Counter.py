'''
https://www.hackerrank.com/challenges/strange-code/problem
'''

import math
import os
import random
import re
import sys

def strangeCounter(t):
    c = 0
    summ = 3
    while True:
        if t<=summ:
            returner = summ-t+1
            break
            
        else:
            c+=1
            summ+=3*2**c
            continue
            
    return returner
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
