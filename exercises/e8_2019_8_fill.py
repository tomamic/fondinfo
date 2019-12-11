def print_matrix(matrix, w, h):
    for y in range(h):
        for x in range(w):
            print("@" if matrix[y*w + x] else "-", end="")
        print()
    print()

def fill(x, y, matrix, w, h):
    if x < 0 or w <= x or y < 0 or h <= y or matrix[y*w + x]:
        return
    matrix[y*w + x] = True
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        fill(x+dx, y+dy, matrix, w, h)

def main():
    w, h, matrix = 6, 6, [False] * 36
    for x, y in ((0, 0), (2, 5), (3, 4), (4, 3), (5, 2)):
        matrix[y*w + x] = True
    print_matrix(matrix, w, h)

    fill(1, 0, matrix, w, h)  # start filling from (1, 0)
    print_matrix(matrix, w, h)
    print(all(matrix))  # are all elements true?

main()
