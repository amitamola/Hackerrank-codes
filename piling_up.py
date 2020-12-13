'''
https://www.hackerrank.com/challenges/piling-up/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT]]

for val in range(int(input())):
    k= 0
    v = int(input())
    
    vals = list(map(int, input().split()))
    
    if 0 in vals:
        print(False)
        continue
        
    if vals[0]==vals[-1]:
        temp = vals[0]
        vals.pop(0)
    elif vals[0]>vals[-1]:
        temp = vals[0]
        vals.pop(0)
    else:
        temp = vals[-1]
        vals.pop(-1)
        
    while len(vals)>0:
        if (vals[0]>temp) or (vals[-1]>temp):
            print('No')
            k = 1
            break
        
        elif vals[-1]==temp:
            temp = vals[-1]
            vals.pop(-1)
        
        elif vals[0]==temp:
            temp = vals[0]
            vals.pop(0)
        
        elif vals[0]>=vals[-1]:
            temp = vals[0]
            vals.pop(0)
            
        else:
            temp = vals[-1]
            vals.pop(-1)
            
    if k==0:
        print('Yes')
