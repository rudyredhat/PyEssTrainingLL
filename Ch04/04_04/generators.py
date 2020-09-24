#!/usr/bin/env python3

# generators are special class of the function that serve as iterators
# instead of returning single value , it returns stream of values
# program below works as range with with including the last value

def main():
    for i in inclusive_range(25):
        print(i, end=' ')
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator is just below this 4 lines of codes
    i = start
    while i <= stop:
        # yield just works as returns in generators
        # so it yield the values and the function and it yields the next val
        yield i
        i += step


if __name__ == '__main__': main()