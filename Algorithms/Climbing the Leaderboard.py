'''
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect


def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    
    size = len(ranked)
    ranks = []
    
    i = 0
    j = len(ranked)-1
    
    while i<len(player):
        if j<0:
            ranks.append(1)
            i+=1
            continue
        
        if player[i]<ranked[j]:
            ranks.append(j+2)
            i+=1
        
        elif player[i]>ranked[j]:
            j-=1
        
        else:
            ranks.append(j+1)
            i+=1
    return ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
