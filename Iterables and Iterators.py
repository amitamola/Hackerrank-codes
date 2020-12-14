'''
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
'''

from itertools import combinations

_ = int(input())

vals = input().split()

r = int(input())

values = list(combinations(vals, r))
print(sum([True if 'a' in a else False for a in values])/len(values))
