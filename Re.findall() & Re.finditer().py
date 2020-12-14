'''
https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
'''

string = input()
pattern = r'([aeiouAEIOU]{2,})[^aeiouAEIOU]{1}'

import re

result = re.findall(pattern, string)
if len(result)==0:
    print(-1)
    
else:
    for val in result:
        print(val)
