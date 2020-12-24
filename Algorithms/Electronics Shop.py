'''
https://www.hackerrank.com/challenges/electronics-shop/problem
'''

import os
import sys
from itertools import product

def getMoneySpent(keyboards, drives, b):
    allout = list(product(keyboards, drives))
    new_sum = -1
    for val in allout:
        if new_sum<sum(val)<=b:
            new_sum = sum(val)
    
    return new_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
