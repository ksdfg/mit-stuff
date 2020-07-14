from random import choice

from math import gcd
from sympy import mod_inverse as modinv


def encrypt_string(key, plaintext):
    d, n = key
    cipher = [(ord(char) ** d) % n for char in plaintext]
    return ''.join(map(lambda i: chr(i), cipher))


def decrypt_string(key, ciphertext):
    e, n = key
    plain = [chr((char ** e) % n) for char in map(lambda i: ord(i), ciphertext)]
    return ''.join(plain)


def generate_keypair(p, q):
    n = p * q

    phi = (p - 1) * (q - 1)

    l = list()
    for x in range(2, phi):
        if gcd(phi, x) == 1 and x != modinv(x, phi):
            l.append(x)
    e = choice(l)

    d = modinv(e, phi)
    return (e, n), (d, n)


primes = [int(input('Enter prime p: ')), int(input('Enter prime q: '))]
pub_key, priv_key = generate_keypair(*primes)
print("public key =", pub_key, "\nprivate key =", priv_key, end='\n\n')

s = input("Enter a message to encrypt: ")
print("Plain message: " + s)
enc = encrypt_string(priv_key, s)
print("Encrypted message: ", enc)
dec = decrypt_string(pub_key, enc)
print("Decrypted message: " + dec)
