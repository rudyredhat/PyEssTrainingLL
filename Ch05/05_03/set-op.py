#!/usr/bin/env python3

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(sorted(a))
    print_set(b)
    # members of set a not in b
    print_set(a - b)
    # both all
    print_set(a | b)
    # exclusive or
    print_set(a ^ b)
    # only in both
    print_set(a & b)



def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')
    # un-ordered unique set is printed, each time
    # {gnb to.Wedai'r}
    # {veiIrnmtyaDochs'f.d, }

if __name__ == '__main__': main()