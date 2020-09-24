#!/usr/bin/python3

# create a tuple with diff types
x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]

print('x is {}'.format(x))

print(type(x[1]))
# id return unique identifier of the unqiue objects
print(id(x[1]))
print(id(x[2]))
# 139960308648240
# 139960308650896
print(id(y[1]))
print(id(y[1]))
# 140429730396528
# 140429730396528

# check for the instance not for the type
if isinstance(y, tuple):
    print("tuple")
elif isinstance(y, list):
    print("list")
else:
    print("nope")