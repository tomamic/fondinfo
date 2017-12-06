actors = ("farmer", "cabbage", "goat", "wolf")
L, R = False, True
wrong = [(L, R, R, L), (L, L, R, R), (L, R, R, R),
         (R, L, L, R), (R, R, L, L), (R, L, L, L)]
        # (cabbage == goat != farmer) or (goat == wolf != farmer)

def print_status(status: (bool, bool, bool, bool)) -> None:
    for a, s in zip(actors, status):
        if s == R:
            print("\t|~| " + a)
        else:
            print(a + "\t|~| ")

def possible_moves(steps: list) -> list:
    moves = []
    # for each actor on the same side as the farmer...
    # try to make it travel along with the farmer
    # (in the case i == 0, the farmer travels alone)
    for i in range(len(actors)):
        status, move = steps[-1], list(steps[-1])
        move[0], move[i] = not status[0], not status[i]
        if status[i] == status[0] and not tuple(move) in wrong + steps:
            moves.append(tuple(move))
    return moves

def solve(steps: list) -> bool:
    if steps[-1] == (R, R, R, R):
        return True
    for move in possible_moves(steps):
        steps.append(move)
        if solve(steps):
            return True
        steps.pop()  # backtracking
    return False

steps = [(L, L, L, L)]
solve(steps)
for status in steps:
    print_status(status)
    print()

##def possible_steps(steps: list) -> list:
##    return [steps + [m] for m in possible_moves(steps)]
##
##def all_solutions(steps: list) -> list:
##    if steps[-1] == (R, R, R, R):
##        return [steps]
##    return sum(map(all_solutions, possible_steps(steps)), [])
##
##print(all_solutions([(L, L, L, L)]))
