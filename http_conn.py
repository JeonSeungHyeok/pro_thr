import socket
ip = '192.168.247.142'
ports = [21,22,23,80,8080,8180,8888]
for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('소켓 생성')
        conn = s.connect_ex((ip, port))
        print(port, ': ', conn)