#!/usr/bin/python3

x = [1, 2, 3, 4, 5]
# list is mutable
# and we can re modify the item from the list
x[2] = 42
for i in x:
    print('i is {}'.format(i))

# dict is mutable
y = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
y['three'] = 42
for k, v in y.items(): # .items() = return 2 tuples each with key and value
    print('k: {}, v: {}'.format(k, v))

# range are immutable , which can be mutable by using list(range(n))