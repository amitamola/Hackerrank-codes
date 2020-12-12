'''
https://www.hackerrank.com/challenges/np-sum-and-prod/problem?h_r=next-challenge&h_v=zen

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
'''

import numpy
n, m = tuple(map(int, input().split()))

vals = []

for a in range(n):
    i = tuple(map(int, input().split()))
    vals.extend(i)
    
vals = numpy.array(vals)
vals = vals.reshape((n,m))

vals = vals.sum(axis=0)
print(vals.prod())
