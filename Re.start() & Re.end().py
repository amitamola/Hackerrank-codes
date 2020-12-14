'''
https://www.hackerrank.com/challenges/re-start-re-end/problem
'''

string = input()
to_find = input()

import re
q=0


if to_find not in string:
    print((-1, -1))

else:
    while True:
        a = re.search(to_find, string[q:])
        
        if a is not None:
            print((q+a.start(), q+a.end()-1))
            q+=a.start()+1
        
        else:
            break
