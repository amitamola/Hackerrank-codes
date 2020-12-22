'''
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''

import math
import os
import random
import re
import sys
import string

alph = string.ascii_lowercase

dicty = dict(zip(alph, range(26)))
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    k = []
    
    for val in set(word):
        k.append(h[dicty[val]])
    
    return (len(word)*max(k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
