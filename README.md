# Socket-Proramming
Implementing simple chat server, and establishing client server socket communication, so that multiple  clients can communicate over the chat server 

So, how it works is like, frst of all there will be two sides communicating the client side and the server side.
Now lets see how that works in python:

first  of all coming to the server socket file i.e sockets.py here.
#we import socket and import threading cause we will be working with multiple threads of the progam here as we know.
#Now we mention the port we wanna bind  our server socket to and also mention the SERVER, which is basically my IPV4 address.
In the HEADER I mention the bytes that I am ready to send or receive.

#Then I make a function as handle_client, which only hhandles one individual client at a time. So here we make thazt function, to handle one client at a time. How that happens is first connection is established , and then the message is decoded, which is then printed.

Then after displaying the message, the ocnnection is closed by the socket server.
Now another thread runs to accept new connections, basically this is running side by side.


||arly we try to establish, a client  side, in python with send connection so as to send, msgs to e received by the server side.


