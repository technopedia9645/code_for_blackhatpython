import socket
host = "www.google.com"
port = 80
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
send = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
b = send.encode('utf-8')
client.send(b)
response = client.recv(4096)
print(response)
