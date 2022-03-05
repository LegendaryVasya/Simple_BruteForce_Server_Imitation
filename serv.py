import socket
import random


abc = 'abcdefghijklmnopqrstuvwxyz1234567890'

def random_password():
    #function - generating random password of length from ... to ...
    return ''.join(random.choice(abc) for i in range(random.randint(4,5)))


message = []


password = random_password()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 9090))
ready = True
try:
    sock.listen(1)
    conn, addr = sock.accept()
    connected = True
    while True:
        data = conn.recv(1024)
        message.append(data.decode('utf8'))
# The server cannot receive more than a ... attempts / request limit
        if len(message) > 10_000_000:
            conn.send('Too many attempts to connect!'.encode('utf8'))
            break
        if not data:
            break
        if data.decode('utf8') == password:
            #conn.send('Connection success!'.encode('utf8'))
            conn.send(str.encode('Connection success!'))
        else:
            conn.send('Wrong password!'.encode('utf8'))
    conn.close()
except:
    pass

print(*message)

