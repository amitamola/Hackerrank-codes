'''
https://www.hackerrank.com/challenges/re-group-groups/problem
'''

string = input()

import re

pattern = r"([a-zA-Z0-9])\1+"

matches = re.search(pattern, string)

print(matches.group(1) if matches else -1)
