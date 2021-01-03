'''
https://www.hackerrank.com/challenges/marcs-cakewalk/problem
'''

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    miles = 0
    
    for it, val in enumerate(sorted(calorie, reverse=True)):
        miles+= (2**it)*val
    
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
