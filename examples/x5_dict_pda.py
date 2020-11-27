states = ["Q0", "Q1", "Q2"]
state = "Q0"
accepting = ["Q2"]
input_alphabet = ["a", "b"]
stack_alphabet = ["Z", "Y", "A"]
stack = ["Z"]
transition = {("Q0", "a", "Z"): ("Q0", ["Y"]),
              ("Q0", "a", "Y"): ("Q0", ["Y", "A"]),
              ("Q0", "a", "A"): ("Q0", ["A", "A"]),
              ("Q0", "b", "Y"): ("Q2", []),
              ("Q0", "b", "A"): ("Q1", []),
              ("Q1", "b", "Y"): ("Q2", []),
              ("Q1", "b", "A"): ("Q1", [])}

for symbol in input("String? "):
    if symbol not in input_alphabet:
        raise ValueError(symbol + "∉Σ, Σ=" + str(input_alphabet))

    head = None if not stack else stack.pop()
    new_state, data = transition.get((state, symbol, head), (None, []))
    stack += data
    print((state, symbol, head), "→", (new_state, data), "§§", stack)
    state = new_state
    if not state: break

print("Result:", state in accepting)