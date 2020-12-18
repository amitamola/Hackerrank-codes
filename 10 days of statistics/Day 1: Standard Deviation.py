'''
https://www.hackerrank.com/challenges/s10-standard-deviation/problem
'''

n = int(input())

vals = tuple(map(int, input().split()))

mean = sum(vals)/n

numerator = sum(list(map(lambda x:(x-mean)**2, vals)))
std = (numerator/n)**(1/2)
print(round(std, 1))
