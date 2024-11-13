num1 = 3.14
print(num1)

num2 = 7/3
print(num2)

num1 = 3.
print(type(num1))

num1 = 3e4
print(num1)

pos_inf = float('inf') # largest possible floating number in python
print(pos_inf) # smallest possible floating number in python

neg_inf = float('-inf') # undefined number such as divided by 0
print(neg_inf)

nan = float('nan')
print(nan)

'''
To Represnt High Precision
'''

from decimal import Decimal, getcontext
getcontext().prec = 100
x = Decimal(1) / Decimal(7)
print(x)
x = Decimal(2) / Decimal(5)
print(x)


