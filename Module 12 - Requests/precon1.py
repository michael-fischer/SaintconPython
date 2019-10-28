import socket

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def scan_port(address, port):
    try:
        s = socket.socket()
        s.connect((address, port))
        return str(port) + ": " + s.recv(1024).decode('utf-8')
    except Exception as e:
        return str(port) + ": " + str(e)


for p in list(fib(25)):
    print(scan_port('precon.hackerschallenge.org', p))