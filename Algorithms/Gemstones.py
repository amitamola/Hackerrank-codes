'''
https://www.hackerrank.com/challenges/gem-stones/problem
'''

import math
import os
import random
import re
import sys

def gemstones(arr):
    all_set = [set(k) for k in arr]
    
    new = all_set[0]
    
    for val in all_set[1:]:
        new = new.intersection(val)
    
    return len(new)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
