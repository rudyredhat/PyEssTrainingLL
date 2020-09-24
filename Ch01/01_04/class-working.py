#!/usr/bin/python3

# In python class is a definition and objects are the instance of the class

class Duck:
    # functions = methods
    # var = property
    # first arguments in the method is always self
    # self = reference to the object when a class creates a obj
    # we can use this self for the var to be used inside class
    sound = "Booowwww"
    def quack(self):
        print("Quackk")
        print(self.sound) # self.var_name
    def walk(self):
        print("Walk")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()