def linear_search(v: list, value, beg, end) -> int:
    '''v: not necessarily sorted'''

    for i in range(beg, end):
        if v[i] == value:
            return i
    return -1


def binary_search(v: list, value, beg, end) -> int:
    '''v: a sorted list;
       search in the range [beg, end)'''

    if beg >= end:
        return -1
    mid = (beg + end) // 2
    if v[mid] > value:
        return binary_search(v, value, beg, mid)
    elif v[mid] < value:
        return binary_search(v, value, mid + 1, end)
    return mid


def find_minimum(v: list, beg, end):
    min_pos = beg
    for i in range(beg + 1, end):
        if v[i] < v[min_pos]:
            min_pos = i
    return min_pos


def find_maximum(v: list, beg, end):
    max_pos = beg
    for i in range(beg + 1, end):
        if v[i] > v[max_pos]:
            max_pos = i
    return max_pos


def swap(v: list, i: int, j: int):
    v[i], v[j] = v[j], v[i]


def bubble_sort(v: list, beg, end):
    ##last_swap = 0
    for i in range(beg, end - 1):
        if v[i] > v[i + 1]:
            swap(v, i, i + 1)
            ##last_swap = i + 1
    end -= 1  ##end = last_swap
    if end - beg > 1:
        bubble_sort(v, beg, end)  # loop


def selection_sort(v: list, beg, end):
    if end - beg <= 1:
        return
    min_pos = find_minimum(v, beg, end)
    swap(v, min_pos, beg)
    selection_sort(v, beg + 1, end)  # loop


def insertion_sort(v: list, beg, end, mid=1):
    if end - mid <= 0:
        return
    i, value = mid, v[mid]
    # find value's place, at its left
    while i > beg and v[i - 1] > value:
        v[i] = v[i - 1]  # shift right
        i -= 1
    v[i] = value
    insertion_sort(v, beg, end, mid + 1)  # loop


def quick_sort(v: list, beg, end):
    if end - beg <= 1:
        return
    mid, pivot = beg, v[end - 1]
    for i in range(beg, end):
        if v[i] <= pivot:
            swap(v, i, mid)
            mid += 1
    quick_sort(v, beg, mid - 1)
    quick_sort(v, mid, end)


def merge(v: list, beg, mid, end: int):
    result = []  # required extra memory
    i1, i2 = beg, mid
    while i1 < mid or i2 < end:
        if i1 < mid and (i2 == end or v[i1] <= v[i2]):
            result.append(v[i1])
            i1 += 1
        else:
            result.append(v[i2])
            i2 += 1
    v[beg:end] = result


def merge_sort(v: list, beg, end: int):
    if end - beg <= 1:
        return
    mid = (beg + end) // 2
    merge_sort(v, beg, mid)
    merge_sort(v, mid, end)
    merge(v, beg, mid, end)


def main():
    names = ["Ada", "Ann", "Bea", "Eva", "Ivy",
             "Kay", "Lea", "Meg", "Sue", "Zoe"]
    i = binary_search(names, "Meg", 0, len(names))
    print(i)
    
    vals = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
    bubble_sort(vals, 0, len(vals))
    print(vals)

if __name__ == "__main__":
    main()