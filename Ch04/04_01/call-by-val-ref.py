#!/usr/bin/python3

# when call by value is done, and when we pass a var to a function ,
# the function operates on the copy of the variable
# the value is passed , but not  the object itself

def main():
    x = 5 # as integer is immutable
    y = x
    y = 3
    # now if x is treated as a list
    # it is being treated as call by reference
    x = [5]  # as integer is mutable
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    print("main---func")
    kitten(x)
    print(f'in main: x is {x}')

def kitten(a):
    print(id(a))
    # so if the copy is passed , so this must have a diff id, but showing the same id number
    a[0] = 5
    print(id(a))
    print("hello")
    print(a)

if __name__ == '__main__': main()
