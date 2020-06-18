#cliemt side socket programming here
"""Let's see now how can we connect to the server"""

import socket


HEADER = 16
PORT =  5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.43.247"
ADDR= (SERVER,PORT)

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length += b' '* HEADER - len(send_length)
    c.send(send_length+message)
    print(c.recv(2048).decode(FORMAT))


send("Hello world whosoever is there")





