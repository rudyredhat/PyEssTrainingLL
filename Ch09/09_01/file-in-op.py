#!/usr/bin/env python3

def main():
    # open() opens the file in the read only mode
    # r, w, a, r+, w+, r+t(read & text mode)
    f = open('lines.txt')
    for line in f:
        # rstrip() which will strip white space and new lines from the file
        print(line.rstrip())

    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

    # read and write in binary file
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        # choose buffer size carefully
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()