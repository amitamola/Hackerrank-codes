'''
https://www.hackerrank.com/challenges/py-check-strict-superset/problem
'''

setA = set(map(int , input().split()))

final = True
for a in range(int(input())):
    setB = set(map(int , input().split()))
    
    if len(setB-setA)==0 and len(setA-setB)>0:
        pass
    else:
        final = False
print(final)
