'''
https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
'''

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    count = 0
    for val in range(len(s)//2):
        count+=(abs(ord(s[val]) - ord(s[len(s)-val-1])))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
