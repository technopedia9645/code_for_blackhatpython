import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

t_host = int(input("enter ip : "))
t_port = int(input("enter port : "))
sock.connect((t_host,t_port))
p = 'GET HTTP/1.1 \r\n'
pe = p.encode('utf-8')
sock.send(pe)
ret = sock.recv(1024)
print ('[+]' + str(ret))
