def combine(alphabet: str, n: int) -> [str]:
    if n == 0:
        return ['']

    combinations = combine(alphabet, n - 1)
    #return [symbol + comb for symbol in alphabet for comb in combinations]

    result = []
    for symbol in alphabet:
        for comb in combinations:
            result.append(symbol + comb)
    return result

print(combine("AEIOU", 3))
