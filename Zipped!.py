'''
https://www.hackerrank.com/challenges/zipped/problem
'''

a, b = tuple(map(int, input().split()))

k = []
for it in range(b):
    k.append(tuple(map(float, input().split())))
    
for val in zip(*k):
    print(round((sum(val)/b), 1))
