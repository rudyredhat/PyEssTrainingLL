#!/usr/bin/env python3

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    for v in animals.keys(): print(v)

    for v in animals. values(): print(v)

    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()