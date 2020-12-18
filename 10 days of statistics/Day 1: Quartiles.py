'''
https://www.hackerrank.com/challenges/s10-quartiles/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

vals = sorted(list(map(int, input().split())))

def odd(values):
    return values[(len(values)-1)//2]

def even(values):
    return (values[len(values)//2]+ values[((len(values))//2)-1])//2
    
if n%2==1:
    q2 = odd(vals)
    q1 = even(vals[:(n-1)//2])
    q3 = even(vals[((n-1)//2)+1:])

else:
    q2 = even(vals)
    if (n//2)%2==1:
        q1 = odd(vals[:(n//2)])
        q3 = odd(vals[(n//2):])
    
    else:
        q1 = even(vals[:(n-1)//2])
        q3 = even(vals[((n-1)//2)+1:])
        
print(q1, q2, q3, sep='\n')
