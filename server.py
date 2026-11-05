from socket import *
import threading

# Fixed header size for messages
HEADERSIZE = 64
serverPort = 19000

def send(sock, text):
    data = text.encode('utf-8')
    header = str(len(data)).encode('utf-8').ljust(HEADERSIZE)
    sock.sendall(header + data)

def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n-len(data))
        if not chunk:
            return None 
        data += chunk
    return data

def receive_loop(sock):
    while True:
        header = recv_exact(sock, HEADERSIZE)
        if header is None:
            print('\nClient disconnected.')
            break
        msg_length = int(header.decode('utf-8').strip())
        msg = recv_exact(sock, msg_length)
        if msg is None:
            print('\nClient disconnected.')
            break
        print('\nFrom client:', msg.decode('utf-8'))

# Create a TCP socket.
serverSocket = socket(AF_INET,SOCK_STREAM)

# Assign the socket a port on this computer.
serverSocket.bind(('',serverPort))

serverSocket.listen(1)
print('The server is ready to receive')

# Wait for a client to connect.
connectionSocket, addr = serverSocket.accept()
print(f'Connected to client at {addr}')

# Start the receive loop in a separate thread.
receiver = threading.Thread(target=receive_loop, args=(connectionSocket,), daemon = True)
receiver.start()

#Main thread
try:
    while True:
        reply = input()
        if reply:
            send(connectionSocket, reply)
except(KeyboardInterrupt, EOFError, OSError):
    pass
finally:
    connectionSocket.close()
    serverSocket.close()

    print('Server closed.')

# # Receive and display the client's message.
# sentence = connectionSocket.recv(1024).decode()
# print('From client:', sentence)

# # Let the server user type a reply.
# reply = input('Message to client: ')

# # Send the reply to the client.
# connectionSocket.sendall(reply.encode())

# # Close both sockets after exchanging messages.
# connectionSocket.close()
# serverSocket.close()