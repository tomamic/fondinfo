class Animal:
    def say(self):
        raise NotImplementedError("Abstract method")

class Dog(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print(self._name, 'says :',  'bau')

class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print(self._name, 'says :',  'miao')

class Pig(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print(self._name, 'says :',  'oink')


# a list of Animal objects
animals = [Dog('danny'), Cat('candy'),
           Pig('peppa'), Pig('george')]

for a in animals:
    a.say()
