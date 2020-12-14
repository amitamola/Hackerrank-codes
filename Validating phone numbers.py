'''
https://www.hackerrank.com/challenges/validating-the-phone-number/problem
'''

import re
for a in range(int(input())):
    num = input()
    
    if len(num)!=10:
        print('NO')
        continue
    
    listy = re.findall(r'([789]{1}[0-9]{9})', num)
    
    if len(listy)==1:
        print('YES')
    else:
        print('NO')
