import socket
import urllib2
import uuid
import base64

urls = []
src_ip = '172.16.0.2'
cnt = 10000000

def url_generator(cnt):    
    for i in range(cnt):

        urls.append('http://' + a[:-2] + '.com')

true_socket = socket.socket

def make_bound_socket(source_ip):
    def bound_socket(*a, **k):
        sock = true_socket(*a, **k)
        sock.bind((source_ip, 0))
        return sock
    return bound_socket

socket.socket = make_bound_socket(src_ip)

class MyException(Exception):
    pass

print('start to execute')
#url_generator(cnt)
for i in range(cnt):
    print('http try {}'.format(i))
    addr = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    addr = 'http://' + addr + '.com'
    try:
        urllib2.urlopen(addr, timeout=1)
    except urllib2.URLError as e:
        #print type(e)    #not catch
        pass
    except socket.timeout as e:
        #print type(e)    #catched
        raise MyException("There was an error: %r" % e)



