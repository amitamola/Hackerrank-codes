'''
https://www.hackerrank.com/challenges/any-or-all/problem
'''

_ = input()

integers = list(map(int, input().split()))

all_p = list(map(lambda x:x>=0, integers))

is_it = False
if all(all_p):
    for val in integers:
        k = str(val)
        
        if k==k[::-1]:
            print(True)
            is_it = True
            break

if is_it == False:
    print(False)
