DISCS = 5
POLES = 3
SUM_OF_POLE_IDS = 2 + 1 + 0

def print_towers(towers: list):
    for t in range(POLES):
        print('|-', end='')
        for d in towers[t]:
            print(d, end='')
        print()
    input()

def move_towers(towers: list, n: int, src: int, dst: int):
    # find the teporary pole (for this plan)
    tmp = SUM_OF_POLE_IDS - src - dst;

    # if there are discs above, move n-1 away
    if n > 1: move_towers(towers, n-1, src, tmp);

    # now move the largest disc (of n) to its dest    
    top_disc = towers[src].pop()
    towers[dst].append(top_disc)
    print_towers(towers)

    # if there were discs above, move those on top
    if n > 1: move_towers(towers, n-1, tmp, dst)

if __name__ == '__main__':
    towers = [[] for p in range(POLES)]
    for d in reversed(range(DISCS)):
        towers[0].append(d + 1)
    print_towers(towers)

    # move all discs from pole 0 to pole 2
    move_towers(towers, DISCS, 0, POLES-1)
