'''
https://www.hackerrank.com/challenges/introduction-to-regex/problem
'''
for val in range(int(input())):
    try:
        num = input()
        
        if num[-1]=='.':
            print(False)
            
        elif '.' not in num:
            print(False)
            
        else:
            num = float(num)
            print(True)
        
    except:
        print(False)
