'''
https://www.hackerrank.com/challenges/runningtime/problem
'''

import math
import os
import random
import re
import sys
    
    
def insertionSort1(n, ar):
    to_sort = ar[-1]
    
    p = len(ar)-2
    
    count = 0
    
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
            count+=1
                    
    return ar, count
    
def runningTime(arr):
    counter = 0
    n=len(arr)
    for i in range(2, len(arr)+1):
        # print(arr[:i])
        first_half, count = insertionSort1(n, arr[:i])
        counter+=count
        second_half = arr[i:]
        
        arr = first_half+second_half
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
