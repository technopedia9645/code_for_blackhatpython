import requests 
import paramiko
import pyfiglet 
import sys
import socket
import tqdm
figletbanner = pyfiglet.figlet_format("c a t ", font = "alligator" )
print(figletbanner)
def help():
   print("**"*50)
   print("enter ip or url, if ip is used enter hhtp or https")
   print("enter <header>  to show webserver header ")
   print('''example : python3 netcatreplace.py 
                      http://127.0.0.1
                      header ''')
   print("enter <ip> to get ip of website ")
   print(''' example : python3 netcatreplace.py
                       http://example.com''')
   print("enter <ssh> to start ssh client ")
   print(''' example : python3 netcatreplace.py
                       ip
                       username
                       password
                       n''')
   print("enter <listen> to start listening on a port")
   print(''' example : python3 netcatreplace.py
                       port to listen on ''')
   print("enter <msf> to start metasploit")
   print(''' example : python3 netcatreplace.py
                       msf ''')
   print("enter <httpserver> to start httpserver")
   print(''' example : python3 netcatreplace.py
                       httpserver ''')
   print("enter <sendfile> to send an file")
   print(''' example : python3 netcatreplace.py
                       sendfile 
                       <ip of server>
                       <filename>''')
   print(''' example : python3 netcatreplace.py
                       receivefile 
                       <ip to receive file from> ''')
   print("**"*50)
help()
victim = input("enter victim url or ip : ")
option = input("enter your choice : ")
if option=="header":
                     r = requests.get(victim)
                     print(r.headers)
if option=="ip":
   input=input("enter url : ")
   IP_addres = socket.gethostbyname(input)
   print("IP Address is:" + IP_addres)
if option=="ssh":
        ip=input("enter ip :")
        port=22
        username= input("enter username : ")
        password= input("enter password : ")
        exit = input("enter n if you want to exit else enter y : ")
        while exit=="n":
          cmd=input("enter command : ") 

          ssh=paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          ssh.connect(ip,port,username,password)

          stdin,stdout,stderr=ssh.exec_command(cmd)
          outlines=stdout.readlines()
          resp=''.join(outlines)
          print(resp)

          stdin,stdout,stderr=ssh.exec_command(cmd)
          outlines=stdout.readlines()
          resp=''.join(outlines)
          print(resp)
          break
if option=="listen":
   
     s = socket.socket()		
     print ("Socket successfully created")
     port =("enter port to listen : ")		
     s.bind(('', port))		
     print ("socket binded to %s" %(port))
     s.listen(5)	
     print ("socket is listening")		
     while True: 
         c, addr = s.accept()	
         print ('Got connection from', addr )
         c.send('Thank you for connecting')
         c.close()
if option=="msf":
   os.system("msfconsole")
   exit()

if option=="httpserver":
   os.system("python3 -m http.server")
   print("http server dtrated on port:8000")
   print("link : http://127.0.0.1:8000")

if option=="sendfile":
   SEPARATOR = "<SEPARATOR>"
   BUFFER_SIZE = 4096 
   host = input("enter ip to send file : ")
   port = 5001
   filename = input("enter file name :")
   print("sending file through port : 5001")
   filesize = os.path.getsize(filename)
   s = socket.socket()
   print(f"[+] Connecting to {host}:{port}")
   s.connect((host, port))
   print("[+] Connected.")
   s.send(f"{filename}{SEPARATOR}{filesize}".encode())
   progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
   with open(filename, "rb") as f:
       while True:
           bytes_read = f.read(BUFFER_SIZE)
           if not bytes_read:
                   break
           s.sendall(bytes_read)
           progress.update(len(bytes_read))
           s.close()
if option=="receivefile":
   SERVER_HOST = input("enter host to connect :")
   SERVER_PORT = 5001
   BUFFER_SIZE = 4096
   SEPARATOR = "<SEPARATOR>"
   s = socket.socket()
   s.bind((SERVER_HOST, SERVER_PORT))
   s.listen(10)
   print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
   print("Waiting for the client to connect... ")
   client_socket, address = s.accept()
   print(f"[+] {address} is connected.")
   received = client_socket.recv(BUFFER_SIZE).decode()
   filename, filesize = received.split(SEPARATOR)
   filename = os.path.basename(filename)
   filesize = int(filesize)
   progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
   with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
            client_socket.close()
   s.close()
else:
   help()
