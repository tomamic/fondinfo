if __name__ == '__main__':
    filenames = []
    words = []

    filename = input('Filename? ')
    while filename != '':
        filenames.append(filename)
        filename = input('Filename? ')

    n = int(input('How many top words? '))

    for filename in filenames:
        with open(filename) as infile:
            file_words = infile.read().split()
        for word in file_words:
            if not word in words:
                words.append(word)

    words.sort(key=lambda x: -len(x))

    for i in range(min(n, len(words))):
        print(words[i])
