'''
https://www.hackerrank.com/challenges/halloween-sale/problem
'''

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    count=0
    
    if s<p:
        return count
    
    while s>=m:
        ded = p-d*count
        
        if s<ded:
            break
        
        elif ded>m:
            s-=(p-d*count)
            count+=1
        else:
            s-=m
            count+=1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
