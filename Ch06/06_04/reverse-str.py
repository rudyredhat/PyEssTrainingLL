#!/usr/bin/env python3

# str here is the built-in class , which is standard string class
class RevStr(str):
    # overriding the str method to print the str backwards
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()