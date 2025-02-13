#!/usr/bin/env python3

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

# **kwargs = keyword arguments
# useful for passing as dict

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()