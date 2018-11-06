def print_matrix(m: list, w: int, h: int):
    for y in range(h):
        for x in range(w):
            print(f"{m[y * w + x]:3}", end="")
        print()

def main():
    w = int(input("w? ")
    h = int(input("h? ")
    n, count = w * h, 1
    last_x, last_y = 0, 0
    matrix = [0] * n
    matrix[0] = count

    while count < n:
        print_matrix(matrix, w, h)
        x = int(input("x? ")
        y = int(input("y? ")
        if 0 <= x < w and 0 <= y < h:
            dx, dy = abs(x - last_x), abs(y - last_y)
            if matrix[y * w + x] == 0 and (dx, dy) in [(2, 1), (1, 2)]:
                count += 1
                matrix[y * w + x] = count
                last_x, last_y = x, y

main()
