'''
https://www.hackerrank.com/challenges/append-and-delete/problem
'''

import math
import os
import random
import re
import sys
from difflib import ndiff

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # s = list(s)
    # t = list(t)

    # if (s==t) and k>=2*len(s):
    #     return "Yes"
    
    # elif (s!=t) and k>=(len(s)+len(t)):
    #     return "Yes"
    
    # st = ''
    # for val in list(ndiff(s, t)):
    #     if val[0]==' ':
    #         st+=val[2]
    #     else:
    #         break
    
    # if (k-len(s)-len(t)-2*len(st))%2==0:
    # # if ((k - len(s) - len(t) + 2 *len(st)) % 2 == 0):
    #     return "Yes"
    
    # else:
    #     return "No"

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
