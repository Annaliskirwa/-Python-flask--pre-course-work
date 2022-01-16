import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to an IP with Port or url
sock.connect(('0.0.0.0', 8080))

#Send some data
sock.send("Twenty-five bytes to send")

#Receive 4096 bytes from a peer
sock.recv(4096)

#Close the socket connection
sock.close()