#!/usr/bin/env python3

class Animal:
    def __init__(self, **kwargs):
        # we are not providing any default values
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']
# so in setter and getter we need to check the value is there and then return
    # so we have use of exception there in the type() method
    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None
# we have 2 new class and we are inheriting the feature from that class
class Duck(Animal):
    def __init__(self, **kwargs):
        # is type is duck , delete that
        # and with super() func we called the parent class initializer with kwargs
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)

if __name__ == '__main__': main()