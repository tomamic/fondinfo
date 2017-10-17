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
        print("I'm " + self._name + " Dog. I say: WOOF!")

class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("I'm " + self._name + " Cat. I say: MIAOW!")

class Pig(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("I'm " + self._name + " Pig. I say: OINK!")


# a list of Animal objects
animals = [Dog('Danny'), Cat('Candy'),
           Pig('Peppa'), Pig('George')]

for a in animals:
    a.say()
