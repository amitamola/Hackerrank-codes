'''
https://www.hackerrank.com/challenges/re-split/problem
'''

regex_pattern = r"[d+(.|,)?]" 	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
