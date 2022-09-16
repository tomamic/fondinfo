alphabet = {"a", "b"}
all_states = {"Q0", "Q1"}
states = {"Q0"}
accepting = {"Q1"}
transition = {("Q0", "a"): {"Q0"},
              ("Q0", "b"): {"Q0", "Q1"}}

string = input("String? ")
for symbol in string:
    if symbol not in alphabet:
        raise ValueError(symbol + "∉Σ, Σ=" + str(alphabet))

    new_states = set()
    for state in states:
        new_states |= transition.get((state, symbol), set())  # union
    print((states, symbol), "→", new_states)
    states = new_states
    if not states: break

print("Result:", states & accepting != set())
