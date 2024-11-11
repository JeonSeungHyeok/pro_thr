import socket

with socket.socket() as s:
        addr = ("0.0.0.0", 8088)
        s.bind(addr)
        s.listen()
        print("start server..")
        conn, addr = s.accept()
        print(f'accept {addr[0]}:{addr[1]}')

        data = conn.recv(1024)
        conn.send("Hi This is Web".encode())


