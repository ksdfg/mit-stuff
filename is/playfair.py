from string import ascii_lowercase

letters = list(ascii_lowercase)
letters.remove('j')
key_square = [['' for _ in range(5)] for _ in range(5)]


def set_key(key_phrase):
    row = col = 0

    # enter the key phrase in the key square
    for i in key_phrase:
        key_square[row][col] = i
        col += 1
        if col > 4:
            col = 0
            row += 1
        letters.remove(i)

    # enter the rest into the key square
    for i in letters:
        key_square[row][col] = i
        col += 1
        if col > 4:
            col = 0
            row += 1

    # display the key_square
    print(*key_square, sep='\n')


def encode(string):
    res = list(string)
    if len(res) % 2 != 0:
        if res[-1] != 'z':
            res.append('z')
        else:
            res.append('x')
    boo = True
    while boo:
        boo = False
        for i in range(0, len(res) - 1, 2):
            if res[i] == res[i + 1]:
                res.insert(i + 1, 'z')
                if len(res) % 2 != 0:
                    if res[-1] != 'z':
                        res.append('z')
                    else:
                        res.append('x')
                boo = True
                break
    print(res)


set_key('monarchy')
encode('heloz')
