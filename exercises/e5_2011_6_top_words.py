if __name__ == '__main__':
    words = []

    filename = input('Filename? ')
    while filename != '':
        with open(filename) as infile:
            file_words = infile.read().split()
            for w in file_words:
                if not w in words:
                    words.append(w)
        filename = input('Filename? ')

    words.sort(key=lambda x: -len(x))

    n = int(input('How many top words? '))
    for i in range(min(n, len(words))):
        print(words[i])
