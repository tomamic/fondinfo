import sys

LENGTH = 16

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('Insert the file name: ')

with open(filename, 'rb') as infile:
    line = []
    count = 0
    byte = infile.read(1)
    while byte != b'':
        print('{:02x} '.format(ord(byte)), end='')
        if b' ' <= byte <= b'~':
            line.append(chr(ord(byte)))
        else:
            line.append(' ')
        count += 1
        if count == LENGTH:
            print('', ''.join(line))
            line = []
            count = 0        
        byte = infile.read(1)

    if len(line) > 0:
        print('   ' * (LENGTH - count), ''.join(line))  # 1234567
