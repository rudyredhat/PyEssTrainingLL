#!/usr/bin/python3

import platform

print('This is python version {}'.format(platform.python_version()))

# check the version using function call


def main():
    message()


def message():
    print('This is python version {}'.format(platform.python_version()))


if __name__ == '__main__': main()

# imp points:
# 1. block does not define scope in python