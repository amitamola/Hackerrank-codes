'''
https://www.hackerrank.com/challenges/s10-interquartile-range/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())

v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

vals = []

for it, v in enumerate(v1):
    vals.extend([v]*v2[it])
    
vals = sorted(vals)

n = len(vals)

def odd(values):
    return values[(len(values)-1)//2]

def even(values):
    return (values[len(values)//2]+ values[((len(values))//2)-1])/2
    
if n%2==1:
    if (n//2)%2==1:
        q1 = odd(vals[:(n//2)])
        q3 = odd(vals[n//2+1:])
    
    else:
        q1 = even(vals[:(n-1)//2])
        q3 = even(vals[((n-1)//2)+1:])

else:
    if (n//2)%2==1:
        q1 = odd(vals[:(n//2)])
        q3 = odd(vals[(n//2):])
    
    else:
        q1 = even(vals[:(n)//2])
        q3 = even(vals[((n)//2):])

print(float(q3-q1))
