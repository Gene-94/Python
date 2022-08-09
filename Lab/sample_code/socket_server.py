import socket 

HOST = 'localhost'
PORT = 1337

#creates a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#waits until someone connects and returns a new socket to that client and its IP address.
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept

print("Connected by",addr)


#reads 1024 bytes in loop, as long as there is data
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)

conn.close()