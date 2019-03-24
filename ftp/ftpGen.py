from ftplib import FTP
import socket
#import urllib2
true_socket = socket.socket

def make_bound_socket(source_ip):
    def bound_socket(*a, **k):
        sock = true_socket(*a, **k)
        sock.bind((source_ip, 0))
        return sock
    return bound_socket

my_ip = '172.16.0.2'
#socket.socket = make_bound_socket(my_ip)

#domain name or server ip:
server_ip = '192.168.3.2'

ftp = FTP()
ftp.set_pasv(False)
ftp.connect(host=server_ip, port=21, timeout=200, source_address= (my_ip, 21) )
ftp.login(user='root', passwd = '')
#ftp.cwd('~/')
#filename = 'exampleFile.txt'
#ftp.storbinary('STOR '+filename, open(filename, 'rb'))
#ftp.quit()
