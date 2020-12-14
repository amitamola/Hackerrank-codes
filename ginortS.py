'''
https://www.hackerrank.com/challenges/ginorts/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = list(input())

lowers = []
uppers = []
even = []
odd = []

for val in inp:
    if val.isdigit():
        p = int(val)
        
        if p%2==0:
            even.append(val)
        else:
            odd.append(val)
    
    else:
        if val.isupper():
            uppers.append(val)
        else:
            lowers.append(val)

lowers = sorted(lowers)
uppers = sorted(uppers)
even = sorted(even)
odd = sorted(odd)

print(''.join(lowers) + ''.join(uppers)+ ''.join(odd)+''.join(even))
            
