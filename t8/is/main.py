from shuffle import set_key, encode, decode

set_key()

string = input('Enter string to encode : ')
print(
    'The encoded string is : ', encode(string),
    '\nThe decoded string is : ', decode(encode(string))
)
