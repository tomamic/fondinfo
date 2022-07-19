#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Animal:
    def say(self):
        raise NotImplementedError("Abstract method")

class Dog(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("I am", self._name, "Dog. I say: WOOF!")

class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("I am", self._name, "Cat. I say: MEOW!")

class Pig(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("I am", self._name, "Pig. I say: OINK!")


# a list of Animal objects
d = Dog("Danny")
c = Cat("Candy")
p1 = Pig("Peppa")
p2 = Pig("George")

animals = [d, c, p1, p2]

for a in animals:
    a.say()
