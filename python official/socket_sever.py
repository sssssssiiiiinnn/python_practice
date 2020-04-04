import socket


HOST = 'localhost'
PORT = 50007


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)