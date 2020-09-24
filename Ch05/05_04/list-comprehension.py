#!/usr/bin/env python3

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = [x for x in seq if x % 3 != 0] # if clause is only allowed after for clause
    # creating list of tuples
    seq4 = [(x, x**2) for x in seq]
    # calling of func
    # rounding of pi to diff values
    from math import pi
    seq5 = [round(pi, i) for i in seq]
    # creating dict
    seq6 = {x: x**2 for x in seq }
    # create set
    seq7 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()