'''
https://www.hackerrank.com/challenges/jim-and-the-orders/problem
'''

import math
import os
import random
import re
import sys

def jimOrders(orders):
    sumi = [sum(k) for k in orders]
    
    return [i[0]+1 for i in sorted(enumerate(sumi), key=lambda x:x[1])]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
