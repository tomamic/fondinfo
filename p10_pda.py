states = {"Q0", "Q1", "Q2"}
state = "Q0"
accepting = {"Q2"}
input_alphabet = {"a", "b"}
stack_alphabet = {"Z", "Y", "A"}
stack = ["Z"]
transition = {("Q0", "a", "Z"): ("Q0", ["Y"]),
              ("Q0", "a", "Y"): ("Q0", ["Y", "A"]),
              ("Q0", "a", "A"): ("Q0", ["A", "A"]),
              ("Q0", "b", "Y"): ("Q2", []),
              ("Q0", "b", "A"): ("Q1", []),
              ("Q1", "b", "Y"): ("Q2", []),
              ("Q1", "b", "A"): ("Q1", [])}

string = input("String? ")
for symbol in string:
    if symbol not in input_alphabet:
        raise ValueError(f"{symbol}∉Σ, Σ={input_alphabet}")

    head = None if not stack else stack.pop()  # head is at list end
    new_state, data = transition.get((state, symbol, head), (None, []))
    stack += data  # stack grows at list end
    print((state, symbol, head), "→", (new_state, data), "§§", stack)
    state = new_state
    if not state: break

print("Result:", state in accepting)
