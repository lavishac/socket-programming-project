CIS 457 - Socket Programming Project
Names: Jeniffer, Ipek, Lavisha
Project Description:
This project uses Python socket programming to establish a TCP connection between a client and a server. Both programs allow users to type and exchange messages. The client and server woek like two-way chat meaning both sides send and receive messages at the same time until one side disconnects.

Files:
- server.py - Creates the server and waits for a client connection, then chats with the client
- client.py - Connects to the server and sends a message.
- readme.txt - Instructions for running the project.

How to Run:
1. Make sure Python 3 is installed.
2. Open two terminal windows.
3. In the first terminal, navigate to the project folder and run:
   python3 server.py
4. In the second terminal, navigate to the same folder and run:
   python3 client.py
5. Type a message in the client terminal or the server terminal and press Enter.
6. The other terminal will display the message received from the client.
7. Both sides can keep sending messages at any time and can send several messages in a row.
8. To end chat press Ctrl+C in either terminal.
9. If the client disconnects the server prints "Client disconnected" or if the server disconnects the client prints "Server disconnected" and then press Ctrl+C to close it.

Additional Information:
- The programs use TCP sockets.
- The server uses port 19000.
- The client connects to 127.0.0.1 (localhost).
- Both programs can run on the same computer.
- Each program uses a separate thread to receive messages, so it can send and receive at the same time.
- Each message is sent with a fixed 64-byte header that holds the message length, so the receiver knows exactly how much to read.
- Empty messages when pressed Enter with nothing typed they are ignored.