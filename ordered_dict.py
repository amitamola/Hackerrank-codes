'''
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, .
The next  lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
dicty = {}
for p in range(int(input())):
    listy = input().split()
    a, b = ' '.join(listy[:-1]), int(listy[-1])
    if a in dicty:
        dicty[a]+=b
    else:
        dicty[a]=b

for val, price in dicty.items():
    print(val, price, sep=' ')
