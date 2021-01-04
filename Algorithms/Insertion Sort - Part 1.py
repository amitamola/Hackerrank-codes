'''
https://www.hackerrank.com/challenges/insertionsort1/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.

def printer(arr):
    for val in arr:
        print(val, end=' ')
    print()
    
def insertionSort1(n, arr):
    to_sort = arr[-1]
    
    p = len(arr)-2
    
    while True:
        if p==-1:
            arr[p+1]=to_sort
            printer(arr)
            break
        
        elif to_sort>=arr[p]:
            arr[p+1]=to_sort
            printer(arr)
            break
        
        else:
            arr[p+1]=arr[p]
            p-=1
            printer(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
