'''
https://www.hackerrank.com/challenges/cavity-map/problem
'''

import math
import os
import random
import re
import sys

def cavityMap(grid):
    copy_grid = grid.copy()
    for i in range(1, len(grid)-1):
        temp = grid[i][0]
        for j in range(1, len(grid)-1):
            cell = int(grid[i][j])
            top = int(grid[i-1][j])
            bot = int(grid[i+1][j])
            left = int(grid[i][j-1])
            right = int(grid[i][j+1])
            
            if all([cell>k for k in [top, bot, left, right]]):
                temp+= 'X'
            else:
                temp+=str(cell)
        temp+= grid[i][-1]
        copy_grid[i]=temp
    return copy_grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
