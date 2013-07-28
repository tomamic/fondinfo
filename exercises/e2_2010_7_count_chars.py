text = ("Python is a general-purpose, high-level programming language "
        + "whose design philosophy emphasizes code readability. Python's "
        + "syntax allows programmers to express concepts in fewer lines "
        + "of code than would be possible in languages such as C, and "
        + "the language provides constructs intended to enable clear "
        + "programs on both a small and large scale.")

chars = input()
count = 0

for c in text:
    for x in chars:
        if c == x:
            count += 1
            break

print(count)


##for c in text:
##    if c in chars:
##        count += 1
