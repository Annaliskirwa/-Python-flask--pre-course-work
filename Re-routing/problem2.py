# Importing the socket library
import socket

# Building the socket objects
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to an IP with Port 8080
serv.bind(('0.0.0.0', 8080))

# Decalaring backlog of size 5
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        #Receive 4096 bytes from a peer
        data = conn.recv(4096)
        if not data: break
        from_client += data
        #Output message
        print (from_client)
        # Sending data to client
        conn.send("<br>The server is up<br>")
    # Closing the connection
    conn.close()
    #Sending a message that the client has been disconnected
    print ('client disconnected')

#On the terminal run python3 problem2.py to run and compile
# Use 2 terminal windows(one server, the other client) at the same time the other uses the below code



# Client socket code
# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('0.0.0.0', 8080))
# client.send("<br>The server is up<br>")
# from_server = client.recv(4096)
# client.close()
# print (from_server)