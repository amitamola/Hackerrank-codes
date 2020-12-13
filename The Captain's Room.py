'''
https://www.hackerrank.com/challenges/py-the-captains-room/problem
'''
from collections import Counter

_ = input()

vals = tuple(map(int, input().split()))

f = Counter(vals)

print(list(f.keys())[list(f.values()).index(1)])
