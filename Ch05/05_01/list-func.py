#!/usr/bin/env python3

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    i = game.index('Paper')
    print(game[i])

    game.append('Computer')

    game.insert(0, 'Computer')

    game.remove('Paper')

    x = game.pop() # remove from end of the list
    # it also return the removed value
    print(x)

    # can be used to remove at particular index
    game.pop(3)

    del game[3]

    del game[1:3:2]
    # remove by slice

    print(','.join(game)) # join the list with delimiter
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()