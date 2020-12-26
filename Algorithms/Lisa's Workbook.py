'''
https://www.hackerrank.com/challenges/lisa-workbook/problem
'''

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    p = 0
    count = 0
    
    for val in arr:
        a = 1 
        
        if val//k!=0:
            for ji in range(val//k):
                p+=1
                
                if p in range(a, a+k):
                    count+=1
                    
                a+=k
            
            if val%k!=0:
                p+=1
                if p in range(a, a+(val%k)):
                    count+=1
            
        else:
            if val%k!=0:
                p+=1
                
                if p in range(a, a+(val%k)):
                    count+=1
                      
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
