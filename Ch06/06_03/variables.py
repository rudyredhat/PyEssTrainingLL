#!/usr/bin/env python3

class Animal:
    # __init__ method which is our constructor
    # defined 3 diff object var
    x = [1,2,3] # this is class variable not obj var
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

    # so it is drawing from the class, not from the object
    # so this is  a eg = encapsulation
    print(a0.x)
    a1.x[0] = 7
    print(a0.x)
if __name__ == '__main__': main()