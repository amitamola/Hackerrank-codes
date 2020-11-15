'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def print_rangoli(size):
    # your code goes here
    import string

    to_print = '-'.join(string.ascii_lowercase[:size])[::-1]
    
    rusty = tuple(range(1, size*2, 2))
    listy = tuple(range(size))
    middle_print = to_print+to_print[::-1][1:]
    
    lengthy = len(middle_print)
    placehold = []
    for val in listy:
        if val==0:
            top= to_print[:rusty[val]]
        else:
            top= to_print[:rusty[val]]
            top = top+top[::-1][1:]
            
        printy = '-'*((lengthy - len(top))//2)+top+'-'*((lengthy - len(top))//2)
        placehold.append(printy)
        print(printy)

    for value in placehold[::-1][1:]:
        print(value)
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
