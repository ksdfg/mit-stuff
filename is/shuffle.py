from collections import defaultdict
from random import choice
from string import ascii_lowercase, ascii_uppercase

letters = list(ascii_lowercase)
cipher_key = defaultdict(lambda: '')


def set_key():
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        while True:
            value = choice(letters)
            if value != lower:
                letters.remove(value)
                cipher_key[lower] = cipher_key[upper] = value
                break

    print('Your alphabet sequence is : ')
    for i in ascii_lowercase:
        print(i, ':', cipher_key[i])
    print()


def encode(string):
    res = list(string)
    for i in range(len(string)):
        res[i] = cipher_key[string[i]]
    return ''.join(res)


def decode(string):
    key_list = list(cipher_key.keys())
    val_list = list(cipher_key.values())
    res = list(string)
    for i in range(len(string)):
        try:
            res[i] = key_list[val_list.index(res[i])]
        except ValueError:
            pass
    return ''.join(res)
