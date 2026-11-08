from socket import *
import threading

# Fixed header size for messages.
# The header tells the other side how long the message is.
HEADERSIZE = 64
serverName = '127.0.0.1'  
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
        chunk = sock.recv(n - len(data))
        if not chunk:       
            return None
        data += chunk
    return data


def receive_loop(sock):
    """Listen for messages forever."""
    while True:
        header = recv_exact(sock, HEADERSIZE)   # first read the length
        if header is None:
            print('\nServer disconnected.')
            break
        msg_length = int(header.decode('utf-8').strip())
        msg = recv_exact(sock, msg_length)      # then read the message
        if msg is None:
            print('\nServer disconnected.')
            break
        print('\nFrom server:', msg.decode('utf-8'))


# Create a TCP socket and connect to the server.
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(f'Connected to server at {serverName}:{serverPort}')

# Start the receive loop in a separate thread.
receiver = threading.Thread(target=receive_loop, args=(clientSocket,), daemon=True)
receiver.start()

# Read what the user types and send it.
try:
    while True:                 # infinite loop: send many messages in a row
        message = input()
        if message:             # ignore empty lines
            send(clientSocket, message)
except (KeyboardInterrupt, EOFError, OSError):
    pass                       
finally:
    clientSocket.close()
    print('Client closed.')