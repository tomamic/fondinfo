alphabet = ["a", "b"]
states = ["QS", "QA", "QB", "QC"]
state = "QS"
accepting = ["QS"]
transition = {("QS", "a"): "QA", ("QS", "b"): "QB",
              ("QA", "a"): "QS", ("QA", "b"): "QC",
              ("QB", "a"): "QC", ("QB", "b"): "QS",
              ("QC", "a"): "QB", ("QC", "b"): "QA"}

string = input("String? ")
for symbol in string:
    if symbol not in alphabet:
        raise ValueError(symbol + "∉Σ, Σ=" + str(alphabet))

    new_state = transition.get((state, symbol), None)
    print((state, symbol), "→", new_state)
    state = new_state
    if not state: break

print("Result:", state in accepting)
