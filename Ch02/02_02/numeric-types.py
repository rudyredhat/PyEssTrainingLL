#!/usr/bin/python3

from decimal import *
# from decimal lib using Decimal class

a = Decimal('.10') # 10 cents in decimal
b = Decimal('.30') # 30 cents in decimal
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
