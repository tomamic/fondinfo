def merge(a: list, b: list) -> list:
    result = []
    while a or b:
        if a and b:
            d = a if a[0] <= b[0] else b
        else:
            d = a if a else b
        result.append(d.pop(0))
    return result

def main():
    data1 = [1, 4, 5, 7]
    data2 = [2, 3, 6, 8, 9, 10]
    merged = merge(data1, data2)
    print(data1, data2, merged)

main()