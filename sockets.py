#putting the sockets.py file(server side socket program) here
import socket
import threading
"""Since this file is for server socket, so we are focusing on that, and we will be dealing with s
while on the client socket side we deal with c"""

PORT=5050
SERVER = "192.168.#"
ADDR = (SERVER, PORT)
HEADER=64
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

"""meant to handle new connections with the individual client, so probably any sort of comm'n that happens
so, like one client and one server."""
def handle_client(conn, addr):
    print("New connections {} connected".format(addr))

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print("{},{}".format(addr,msg))

    conn.close()

"""This function is meant to kinda handle just any new connections and all."""
def start():
    s.listen()
    print("Server is listening on {}".format(SERVER))



    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args= (conn,addr))
        thread.start()
        print("Active connections is {}".format(threading.active_count()-1))
        conn.send("Msg receiveeed".encode(FORMAT))

print("Server is starting..")

start()

