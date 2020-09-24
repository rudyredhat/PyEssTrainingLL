#!/usr/bin/env python3

x = '47'
y = int(x)
# abs, divmod(x, 3), complex(x, 3)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'the number is {self._n}'

s = 'Hello World'
print(repr(s))
s = bunny(47)
# best possible string representation
# so if we have a class and we can rechange the repr function
print(repr(s))

# so we have ascii() and char(), ord('') func in the same way

# --------------------------
x = ( 1, 2, 3, 4, 5)
y = x
y = reversed(x)
# <reversed object at 0x7efcfe163f70>
y = list(reversed(x))
# [5, 4, 3, 2, 1]
print(x)
print(y)
# in the same way we have sum(), max(), min(), any(), all(), zip(x, y), enumerate()

# ----------------------------
