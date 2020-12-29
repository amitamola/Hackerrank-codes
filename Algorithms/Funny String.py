'''
https://www.hackerrank.com/challenges/funny-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rev = s[::-1]
    
    l1 = [ord(x) for x in s]
    l2 = [ord(x) for x in rev]
    
    l1_out = []
    l2_out = []
    
    for val in range(len(l1)-1):
        l1_out.append(abs(l1[val]-l1[val+1]))
        l2_out.append(abs(l2[val]-l2[val+1]))
        
    if l1_out==l2_out:
        return 'Funny'

    else:
        return 'Not Funny'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
