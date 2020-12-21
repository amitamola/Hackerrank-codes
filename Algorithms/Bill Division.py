'''
https://www.hackerrank.com/challenges/bon-appetit/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    she_ate = bill.copy()
    she_ate.pop(k)
    
    if sum(she_ate)/2==b:
        print('Bon Appetit')
    
    else:
        print((b-sum(she_ate)//2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
