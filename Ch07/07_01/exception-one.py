#!/usr/bin/env python3

# powerful runtime error reporting mechanism
# last line we have the error and everything is called as the tarce back
import sys
# we can import sys for extra info about the error using sys.exec_info()
def main():
    try:
        x = int('foo')
    except ValueError:
        print(f'I caught a value error: {sys.exc_info()}')
    except ZeroDivisionError:
        print('dont divide by zero')
    except:
        print('Unknown error')
    # so we can capture the error and the execution will continue without problem
    print('Hello, World.')

if __name__ == '__main__': main()