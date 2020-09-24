#!/usr/bin/env python3

# it is form of meta programming , special type of func returns wrapper function
# in python everything is object

def f1():
    print('Hello, World.')

# assigning the function obj to var x
x = f1
x()

# but we cannot call functions of inherit function, because it is out of scope
def f1(f):
    def f2():
        print('before call')
        f()
        print('after call')
    return f2
# creating decorator to call f2()
@f1
def f3():
    print("this is f3")
f3()
'''
x = f1(f3)
x()
print("-----")
# now f3 is used as decorator below
f3 = f1(f3)
f3()
print("------")
'''
# so this can be used above as a wrapper function
# use -- @f1 -- just above f3()