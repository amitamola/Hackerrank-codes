'''
https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    answer = "NO"
    start = s[0]
    k1 = 0
    k2 = 1
    ori = 1
    
    while True:
        next_val = str(int(s[k1:k2])+1)
        checker = s[k2:k2+len(next_val)]
        
        if k2>=len(s):
            answer = "YES"
            break
            
        if next_val==checker:
            k1=k2
            k2=k2+len(next_val)
            
        else:
            ori+=1
            k1=0
            k2=ori
            start = s[k1:k2]
            
    if start==s:
        print("NO")
    else:
        print(answer, start)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
