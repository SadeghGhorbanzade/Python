#!/usr/bin/python

import socket

class newSocket():
    def __init__(self, port):
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.port = port
        self.sock.bind((self.host, self.port))

s = newSocket(80)





## Networking
##class user(userID, ip):
##    def __init__(self):
##        self.userID = userID
##        self.ip = ip


## Interface
