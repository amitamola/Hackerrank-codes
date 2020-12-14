'''
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
'''

cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    p = [0,1]
    
    if n==0:
        return []
    
    elif n==1:
        return p[0:1]
    
    elif n==2:
        return p
    
    else:
        for val in range(n-2):
            p.append(p[-1]+p[-2])
        
    return p

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
