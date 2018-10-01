def anagram(text: str) -> [str]:
    if len(text) == 0:
        return ['']

    result = []
    for i in range(len(text)):
        c = text[i]
        rest = text[:i] + text[i + 1:]
        for p in anagram(rest):
            result.append(c + p)
    return result

print(anagram("RAMO"))
