import socket
import threading

# we pass in the IP address and port we want the server to listen on
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Next we tell the server to start listening
server.bind((bind_ip, bind_port))

# with a maximum backlog of connections set to 5
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# this is our client handling thread
def handle_client(client_socket):
    # just print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    client_socket.send(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()


# We  put the server into its main loop, where it is waiting for an incoming connection.
while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
