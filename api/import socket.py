import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# bind the socket to a public host and a well-known port
port = 12345
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, address = server_socket.accept()

    # receive data from the client
    data = client_socket.recv(1024).decode()

    if data == "s 0":
        print("Server started the connection.")
        # do something to start the connection
    elif data == "t 0":
        print("Server closed the connection.")
        # do something to close the connection
        client_socket.close()
        break

# close the server socket
server_socket.close()
