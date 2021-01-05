'''
https://www.hackerrank.com/challenges/weighted-uniform-string/copy-from/194283041
'''

import math
import os
import random
import re
import sys
from string import ascii_lowercase

def weightedUniformStrings(s, queries):
    dicty = dict(zip(ascii_lowercase, range(1,27)))

    place_h = s[0]
    weights = set()
    weights.add(dicty[place_h])
    
    count = 1
    for val in s[1:]:
        if val==place_h:
            count+=1
            weights.add(count*dicty[val])
            
        else:
            count=1
            place_h = val
            weights.add(dicty[val])
            
    result = ['Yes' if k in weights else 'No' for k in queries]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
