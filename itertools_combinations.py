'''
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''

from itertools import combinations

word, r = input().split()

to_p = []

for v in range(1,int(r)+1):
    to_p.append(tuple(combinations(sorted(word), int(v))))

for listy in to_p:
    for word in listy:print(''.join(word))
