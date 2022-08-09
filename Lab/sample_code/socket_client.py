import socket 

HOST = 'localhost'
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send("All your base are belong to us")
data = s.recv(1024)

s.close()

print("Received", repr(data))