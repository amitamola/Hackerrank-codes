'''
https://www.hackerrank.com/challenges/kaprekar-numbers/problem
'''

import math
import os
import random
import re
import sys

def is_kap(num):
    le = len(str(num))
    num2 = num**2
    
    if len(str(num2))==len(str(num)):
        if num2==num:
            return True
        else:
            return False
        
    r = int(str(num2)[-le:])
    l = int(str(num2)[:-le])
    
    if (l+r)==num:
        return True

    else:
        return False
    
def kaprekarNumbers(p, q):
    count = 0
    
    for num in range(p,q+1):
        if is_kap(num):
            print(num, end=' ')
            count+=1
    
    if count==0:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
