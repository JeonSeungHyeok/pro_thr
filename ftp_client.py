from ftplib import FTP
ftp = FTP('192.168.247.137')
ftp.set_pasv(True)  # Passive Mode 활성화
print('login: ',ftp.login('ftpuser','1')) # 익명 접속 허용하면 매개변수 필요없음
print('banner: ',ftp.getwelcome()) # 배너 확인
print('pwd: ',ftp.pwd()) # 현재 작업 경로 확인
print('LIST: ',ftp.retrlines('LIST')) # 소켓을 알아서 열고 닫음 -> 포트지정 안해도 됨
#print(ftp.retrbinary('RETR a.txt', open('bvc.txt', 'wb').write)) # retrieve 다운로드(쓰기)
print(ftp.retrbinary('STOR move1.txt', open('bbb.txt', 'rb'))) # store 다운로드(읽기)