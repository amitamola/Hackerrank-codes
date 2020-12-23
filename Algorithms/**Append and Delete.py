'''
https://www.hackerrank.com/challenges/append-and-delete/problem
'''

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    if ((len(s) + len(t)) < k): 
        return "Yes"
  
    commonLength = 0
    for i in range(0, min(len(s), len(t)), 1): 
        if (s[i] == t[i]): 
            commonLength += 1
        else: 
            break
    
    d= k - len(s) - len(t) + 2*commonLength
    
    if(d>=0) and (d%2==0): 
        return "Yes"
  
    return "No"
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
