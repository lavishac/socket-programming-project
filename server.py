from socket import *

serverPort = 19000

# Create a TCP socket.
serverSocket = socket(AF_INET,SOCK_STREAM)

# Assign the socket a port on this computer.
serverSocket.bind(('',serverPort))

# Listen for a client connection.
serverSocket.listen(1)
print('The server is ready to receive')

# Wait for a client to connect.
connectionSocket, addr = serverSocket.accept()

# Receive and display the client's message.
sentence = connectionSocket.recv(1024).decode()
print('From client:', sentence)

# Let the server user type a reply.
reply = input('Message to client: ')

# Send the reply to the client.
connectionSocket.sendall(reply.encode())

# Close both sockets after exchanging messages.
connectionSocket.close()
serverSocket.close()