'''
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints



Input Format

The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .

Output Format

Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print .
'''

len1, len2 = tuple(map(int, input().split(' ')))

group_a = [str(input()) for a in range(len1)]
group_b = [str(input()) for a in range(len2)]

for val in group_b:
    k=0
    if val in group_a:
        while val in group_a[k:]:
            ind = group_a[k:].index(val)
            print(k+ind+1, end=' ')
            k+=ind+1
        print()
    else:
        print(-1)
