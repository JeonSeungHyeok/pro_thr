import socket, sys, errno

remoteServer = input('점검할 호스트 IP를 입력: ')
remoteServerIP = socket.gethostbyname(remoteServer)
print('스캔할 포트 범위를 입력하세요')
startPort = input('시작포트: ')
endPort = input('마지막 포트 번호: ')
print('스캔 중입니다. 호스트: ', remoteServerIP)

try:
    for port in range(int(startPort), int(endPort)):
        print('Checking port {}...'.format(port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            conn = s.connect_ex((remoteServerIP, port))
            if conn == 0:
                print('Port {}: Open'.format(port))
            else:
                print('Port {}: Closed'.format(port))
                print('Reason: ', errno.errorcode[conn])
except Exception as e:
    print('서버에 연결할 수 없어요')