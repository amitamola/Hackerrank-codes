'''
https://www.hackerrank.com/challenges/py-check-subset/problem
'''

for val in range(int(input())):
    a = int(input())
    a_vals = set(map(int, input().split()))
    
    b = int(input())
    b_vals = set(map(int, input().split()))
    
    if len(a_vals-b_vals)==0:
        print(True)
    else:
        print(False)
