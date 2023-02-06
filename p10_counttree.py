def count_tree(t: int | list) -> int:
    count = 0
    if isinstance(t, list):
        for v in t:
            count += count_tree(v)
    else:
        count += 1
    return count

tree = [[1, 2, [3, 4], [5]], 6]
print(count_tree(tree))