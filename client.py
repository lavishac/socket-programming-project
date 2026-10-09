from socket import *

# Use this computer's IP address and the server's port.
serverName = '127.0.0.1'
serverPort = 19000

# Create a TCP socket and connect to the server.
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Get the user's message and send it as bytes.
sentence = input('Input a sentence:')
clientSocket.send(sentence.encode())

# Receive the server's reply and convert it to text.
reply = clientSocket.recv(1024)
print ('From Server:', reply.decode())

# Close the connection.
clientSocket.close()