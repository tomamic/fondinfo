PACMAN, WALL, COOKIE, POWERUP, EMPTY = "C#-+ "

def expand_wall(matrix, x, y) -> tuple[int, int]:
    cols, rows = len(matrix[0]), len(matrix)
    w, h = 0, 0
    while x + w < cols and matrix[y][x + w] == WALL:
        w += 1
    while y + h < rows and matrix[y + h][x : x + w] == [WALL] * w:
        matrix[y + h][x : x + w] = [EMPTY] * w
        h += 1
    return w, h

def main():
    walls, cookies, powerups, pacman = [], [], [], None
    with open("p07_pacmanmap.txt") as file1:
        board = [list(line.rstrip("\n")) for line in file1]
    cols, rows = len(board[0]), len(board)
    for y in range(rows):
        for x in range(cols):
            c = board[y][x]
            if c == WALL:
                w, h = expand_wall(board, x, y)
                walls.append((x*8, y*8, w*8, h*8))
            elif c == COOKIE:
                cookies.append((x*8+6, y*8+6))
            elif c == POWERUP:
                powerups.append((x*8+4, y*8+4))
            elif c == PACMAN:
                pacman = (x*8, y*8)

    with open("p05_pacmanmap.py", "w") as file2:
        print("size =", (cols*8, rows*8), file=file2)
        print("pacman =", pacman, file=file2)
        print("walls =", walls, file=file2)
        print("cookies =", cookies, file=file2)
        print("powerups =", powerups, file=file2)

main()
