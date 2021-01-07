from random import choice
from hashlib import sha512
from socket import socket
from string import ascii_letters, digits

if __name__ == "__main__":
    sock = socket()
    _hash = sha512()

    # Generate random string and update hash object
    data = ''.join(choice(ascii_letters + digits) for _ in range(64)).encode()
    print("Generated random string:", data.decode(), sep="\n")
    _hash.update(data)
    computed_hash = _hash.hexdigest()

    # Connecting to the server
    sock.connect(('localhost', 6969))

    # Sending the data
    print("\nSending data")
    sock.send(data.ljust(4096))

    # Print received data
    received_data = sock.recv(4096).decode().strip()
    print(f"\nRecieved data:", received_data, sep="\n")

    # Compute hash of received data
    _hash = sha512()
    _hash.update(received_data.encode())
    received_hash = _hash.hexdigest()

    # Compare the hashes
    if received_hash == computed_hash:
        print("\nSHA-512 of received data is correct!")
    else:
        print(
            f"\nSHA-512s of received data is incorrect"
            f"\nExpected value =  {computed_hash}"
            f"\nActual value = {received_hash}"
        )

    print("\nConnection over")
