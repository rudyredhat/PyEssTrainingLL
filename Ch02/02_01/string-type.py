#!/usr/bin/python3

x = 'seven "{1:<09}" "{0:>09}"'.format(8,9)

# use of extra space or identation
# swap the values in the format
# x is seven "9        " "        8"

# we can have white spaces with 0 fills, add 9 in front of both 9
# x is seven "900000000" "000000008"

print('x is {}'.format(x))
print(type(x))


# use of f string is useful after 3.6
a = 8
b = 9
x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))
