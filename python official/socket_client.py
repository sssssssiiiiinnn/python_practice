import socket


HOST = 'localhost'
PORT = 50007


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input().encode('utf-8')
        s.sendall(msg)
        data = s.recv(1024)
        print(f'Received {data}')