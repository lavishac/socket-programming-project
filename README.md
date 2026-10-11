CIS 457 - Socket Programming Project
Names: Jeniffer, Ipek, Lavisha
Project Description:
This project uses Python socket programming to establish a TCP connection between a client and a server. Both programs allow users to type and exchange messages.

Files:
- server.py - Creates the server and waits for a client connection.
- client.py - Connects to the server and sends a message.
- readme.txt - Instructions for running the project.

How to Run:
1. Make sure Python 3 is installed.
2. Open two terminal windows.
3. In the first terminal, navigate to the project folder and run:
   python3 server.py
4. In the second terminal, navigate to the same folder and run:
   python3 client.py
5. Type a message in the client terminal and press Enter.
6. The server will display the message received from the client.
7. Type a response in the server terminal and press Enter.
8. The client will display the server's response.
9. Both programs will terminate after exchanging messages.

Additional Information:
- The programs use TCP sockets.
- The server uses port 19000.
- The client connects to 127.0.0.1 (localhost).
- Both programs can run on the same computer.