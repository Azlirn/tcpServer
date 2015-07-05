# Written by Azlirn
# Based on script from Black Hat Python

# Can be used for writing command shells, crafting proxies, or more.

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pass in the IP address and port you want the server to listen on.
server.bind(bind_ip, bind_port)

# Tell the server to start listening
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# This is our client-handling threading
# This function performs the recv() and then sends a simple message back to the
# client
def handle_client(client_socket):

    # Print out what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # Send a packet back
    client_socket.send("ACK!")

    client_socket.close()

while True:

    # When a client connects, receive the client socket into the client variable
    # and the remote connection details into the addr variable
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    # Spin up the client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))

    # Main server loop us ready to handle another incoming connection.
    client_handler.start()
