'''
https://www.hackerrank.com/challenges/drawing-book/problem
'''

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p==1 or n==p:
        return 0
    
    elif (n%2==0) and (n==p):
        return 0
    
    elif (n%2!=0) and (p==(n-1)):
        return 0
    
    else:
        count1 = 0
        count2 = 0
        
        if (n%2==0):
            for val in range(2, n, 2):
                count1+=1
                if (p==val) or (p==val+1):
                    break

            for val in range(n-1, 2, -2):
                count2+=1
                if (p==val) or (p==val-1):
                    break
        
        else:
            for val in range(2, n+1, 2):
                count1+=1
                if (p==val) or (p==val+1):
                    break

            for val in range(n-2, 2, -2):
                count2+=1
                if (p==val) or (p==val-1):
                    break 
            
        return min(count1, count2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
