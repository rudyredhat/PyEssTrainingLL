#!/usr/bin/env python3

class Animal:
    # here is the class constructor
    # special method name with __init__ = with acts as an initializer or constructor
    def __init__(self, type, name, sound): # self is the first argument, that whats makes it a obj method

    # we have **kwargs and we can set the default values as well
    #  def __init__(**kwargs):
        # self._type = kwargs['type'] if 'type' in kwargs else 'kitten'

    # below are the object var with _ in the start
        self._type = type
        self._name = name
        self._sound = sound
    # below are the accessors or getters which simply return the value of those object variables
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    # here we use those getters to access the variables
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    # 2 obj from the animal class & intialize with various parameters
    # obj is created using the class name or the func name
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')

    # we can use **kwargs as well
    # a3 = Animal(type='kitten',name='fluffy', sound='rwar')

    print_animal(a0)
    print_animal(a1)
    # directly we are calling here from the constructor
    # function parameters = assignments in python
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()