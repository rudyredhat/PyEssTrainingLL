#!/usr/bin/env python3

def main():
    kitten('meow', 'grrr', 'purr')

# *args = list arguments
# use of multiple list ele
# this is useful when function have number of arguments

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()