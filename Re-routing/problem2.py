import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connect to an IP with Port or url
sock.connect(('0.0.0.0', 8080))