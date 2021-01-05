'''
https://www.hackerrank.com/challenges/caesar-cipher-1/problem
'''

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    new_s = ''
    
    for val in s:
        if val.isupper():
            zi = ord(val)
            if zi+(k%26)>90:
                change = (zi+(k%26))%90+64
                
            else:
                change = zi+(k%26)
                        
        elif val.islower():
            zi = ord(val)
            if zi+(k%26)>122:
                change = (zi+(k%26))%122+96
                
            else:
                change = zi+(k%26)
                
        else:
            change = ord(val)
            
        new_s+=chr(change)
    
    return new_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
