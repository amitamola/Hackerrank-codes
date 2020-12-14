'''
https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
'''

import re
N = int(input())

for i in range(N):
    print (re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))
