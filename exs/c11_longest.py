T = str | list["T"]

def longest(tree: T):
    if not isinstance(tree, list):
        return tree
    if tree == []:
        return ""
    #return max((longest(n) for n in tree), key=len)
    max_word = ""
    for n in tree:
        word = longest(n)
        if len(word) > len(max_word):
            max_word = word
    return max_word

tree = [["spam"], [["egg", "sausage"], [], "spam"]]
print(longest(tree))