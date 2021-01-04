'''
https://www.hackerrank.com/challenges/insertionsort2/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def printer(ar):
    for val in ar:
        print(val, end=' ')
    print()
    
def insertionSort1(n, ar):
    to_sort = ar[-1]
    
    p = len(ar)-2
    
    while True:
        if p==-1:
            ar[p+1]=to_sort
            break
        
        elif to_sort>=ar[p]:
            ar[p+1]=to_sort
            break
        
        else:
            ar[p+1]=ar[p]
            p-=1
            
    return ar
    
def insertionSort2(n, arr):
    for i in range(2, len(arr)+1):
        # print(arr[:i])
        first_half = insertionSort1(n, arr[:i])
        second_half = arr[i:]
        
        arr = first_half+second_half
        printer(arr)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
