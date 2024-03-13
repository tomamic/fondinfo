#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

states = {"Q0", "Q1", "Q2", "Q3", "Q4", "Qf"}
state = "Q0"
accepting = {"Qf"}
alphabet = {"a", "b", "c", "X", "Y", "Z", "$"}
tape = ["$", "a", "a", "a", "b", "b", "b", "c", "c", "c", "$"]
pos = 1
transition = {("Q0", "a"): ("Q1", "X", 1),
              ("Q0", "Y"): ("Q4", "Y", 1),
              ("Q1", "Y"): ("Q1", "Y", 1),
              ("Q1", "a"): ("Q1", "a", 1),
              ("Q1", "b"): ("Q2", "Y", 1),
              ("Q2", "Z"): ("Q2", "Z", 1),
              ("Q2", "b"): ("Q2", "b", 1),
              ("Q2", "c"): ("Q3", "Z", -1),
              ("Q3", "Z"): ("Q3", "Z", -1),
              ("Q3", "Y"): ("Q3", "Y", -1),
              ("Q3", "b"): ("Q3", "b", -1),
              ("Q3", "a"): ("Q3", "a", -1),
              ("Q3", "X"): ("Q0", "X", 1),
              ("Q4", "Y"): ("Q4", "Y", 1),
              ("Q4", "Z"): ("Q4", "Z", 1),
              ("Q4", "$"): ("Qf", "$", 0)}

while state not in accepting:
    symbol = tape[pos]
    if symbol not in alphabet:
        raise ValueError(f"{symbol}∉Σ, Σ={alphabet}")

    trans = transition.get((state, symbol), (None, "", 0))
    new_state, new_symbol, delta = trans
    print((state, symbol), "→", trans, "§§", tape, pos)
    tape[pos] = new_symbol
    state, pos = new_state, pos + delta
    if not state: break

print("Result:", state in accepting)
