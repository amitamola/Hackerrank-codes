'''
https://www.hackerrank.com/challenges/maximize-it/problem
'''

from itertools import product

k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))
results = map(lambda x: sum(i**2 for i in x) % m, product(*n))

print(max(results))
