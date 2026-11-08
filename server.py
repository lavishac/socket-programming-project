from socket import *
import threading
import os
import signal

# Fixed header size for messages.
HEADERSIZE = 64
serverPort = 19000

def send(sock, text):
    """Send one message: header (length) + the message itself."""
    data = text.encode('utf-8')
    header = str(len(data)).encode('utf-8').ljust(HEADERSIZE)
    sock.sendall(header + data)

def recv_exact(sock, n):
    """Read exactly n bytes. Return None if the other side closed."""
    data = b''
    while len(data) < n:
        chunk = sock.recv(n-len(data))
        if not chunk:
            return None 
        data += chunk
    return data

def stop_server():
    """Stop the server when the client disconnects."""
    # Send Ctrl+C to our own program. This wakes the main thread from input().
    os.kill(os.getpid(), signal.SIGINT)

def receive_loop(sock):
    """Listen for messages forever."""
    while True:
        header = recv_exact(sock, HEADERSIZE)
        if header is None:
            print('\nClient disconnected.')
            stop_server()
            break
        msg_length = int(header.decode('utf-8').strip())
        msg = recv_exact(sock, msg_length)
        if msg is None:
            print('\nClient disconnected.')
            stop_server()
            break
        print('\nFrom client:', msg.decode('utf-8'))

# Create a TCP socket.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # allow reusing the port right away

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

# Main thread
try:
    while True:
# infinite loop: read what the user types and send it
        reply = input()
        if reply:
# ignore empty lines
            send(connectionSocket, reply)
except(KeyboardInterrupt, EOFError, OSError):
    pass
finally:
    connectionSocket.close()
    serverSocket.close()

    print('Server closed.')