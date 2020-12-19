'''
https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def remove_items(test_list, item): 
    # using list comprehension to perform the task 
    res = [i-item for i in test_list if i != item] 
  
    return res

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    k = []
    k.append(len(arr))
    
    while len(arr)>1:
        arr = remove_items(arr, min(arr))
        
        if len(arr)!=0:
            k.append(len(arr))
        
    return k
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
