#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Vehicle:
    def estimate_time(self, x: float, y: float) -> float:
        raise NotImplementedError("Abstract Method")
    def name(self) -> str:
        raise NotImplementedError("Abstract Method")

class Ambulance(Vehicle):
    def __init__(self, name: str, x: float, y: float):
        self._name = name
        self._x, self._y = x, y
        self._latency = 1       # min
        self._speed = 90 / 60   # km/min

    def estimate_distance(self, x: float, y: float) -> float:
        return abs(x - self._x) + abs(y - self._y)

    def estimate_time(self, x: float, y: float) -> float:
        return self._latency + self.estimate_distance(x, y) / self._speed

    def name(self) -> str:
        return self._name

class Helicopter(Vehicle):
    def __init__(self, name: str, x: float, y: float):
        self._name = name
        self._x, self._y = x, y
        self._latency = 5       # min
        self._speed = 250 / 60  # km/min

    def estimate_distance(self, x: float, y: float) -> float:
        return ((x - self._x) ** 2  + (y - self._y) ** 2) ** 0.5

    def estimate_time(self, x: float, y: float) -> float:
        return self._latency + self.estimate_distance(x, y) / self._speed

    def name(self) -> str:
        return self._name

def generate_file():
    import random
    with open("vehicles.csv", "w") as csv_out:
        for i in range(10):
            print(random.choice(['A', 'H']), f"V{i:03}",
                  random.uniform(0, 50), random.uniform(0, 50),
                  sep=",", file=csv_out)

def main():
    vehicles = []
    with open("vehicles.csv", "r") as csv:
        for line in csv:
            tp, name, x, y = line.split(",")
            if tp == 'A':
                v = Ambulance(name, float(x), float(y))
                vehicles.append(v)
            else:
                v = Helicopter(name, float(x), float(y))
                vehicles.append(v)

    x, y = float(input("x? ")), float(input("y? "))
    while x >= 0 and y >= 0:
        best_v, best_t = None, 0
        for v in vehicles:
            t = v.estimate_time(x, y)
            if best_v == None or t < best_t:
                best_v, best_t = v, t
        print(best_v.name(), best_t, "\n")
        x, y = float(input("x? ")), float(input("y? "))
