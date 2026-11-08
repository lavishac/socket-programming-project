# socket-programming-project
CIS 457 - Socket Programming Project Names: Jeniffer, Ipek, Lavisha Project Description: This project uses Python socket programming to establish a TCP connection between a client and a server. Both programs allow users to type and exchange messages.

Files:

server.py - Creates the server and waits for a client connection.
client.py - Connects to the server and sends a message.
readme.txt - Instructions for running the project.
How to Run:

Make sure Python 3 is installed.
Open two terminal windows.
In the first terminal, navigate to the project folder and run: python3 server.py
In the second terminal, navigate to the same folder and run: python3 client.py
Type a message in the client terminal and press Enter.
The server will display the message received from the client.
Type a response in the server terminal and press Enter.
The client will display the server's response.
Both programs will terminate after exchanging messages.
Additional Information:

The programs use TCP sockets.
The server uses port 19000.
The client connects to 127.0.0.1 (localhost).
Both programs can run on the same computer.
