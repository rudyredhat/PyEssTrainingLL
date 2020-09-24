#!/usr/bin/python3

# while loop, unless the condition is true, then print the statement
# eg 1
words = ['one', 'two', 'three', 'four', 'five']

n=0
while(n < 5):
    print(words[n])
    n += 1

# eg 2 - fibonnaci series
a, b = 0, 1 # variable declaration **
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a+b
print() # line ending

# eg 3 - for loop
for i in words:
    print(i)