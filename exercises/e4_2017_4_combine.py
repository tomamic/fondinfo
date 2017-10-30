def combine(alphabet: str, n: int) -> [str]:
    if n == 0:
        return ['']

    result = []
    combinations = combine(alphabet, n - 1)
    for symbol in alphabet:
        for comb in combinations:
            result.append(symbol + comb)
    return result

print(combine("AEIOU", 3))
