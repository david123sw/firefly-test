#coding:utf8

import time
import sys

from socket import AF_INET,SOCK_STREAM,socket
from thread import start_new
import struct
from twisted.python import log

HOST='localhost'
PORT=1000
BUFSIZE=1024
MSG_PARSE_TAG = '!sssss3I'
ADDR=(HOST , PORT)
client = socket(AF_INET,SOCK_STREAM)
#TODO:exception
client.connect(ADDR)

def sendData(commandId, sendStr):
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    header = struct.pack(MSG_PARSE_TAG, HEAD_0, HEAD_1, HEAD_2, HEAD_3, ProtoVersion, ServerVersion, len(sendStr)+4, commandId)
    sendStr = header + sendStr
    client.sendall(sendStr)
    return sendStr

def recvData(data):
    if 0 >= len(data):
        log.msg('Sorry, server crash')
        sys.exit(0)
    return None
    head = struct.unpack(MSG_PARSE_TAG,data[:17])
    length = head[6]
    data = data[17:17+length]
    return data

s1 = time.time()
log.msg(s1)

start_new(sendData,(1000, "msg:1000 from client"))
start_new(sendData,(1001, "msg:1001 from client"))
start_new(recvData,(client.recv(BUFSIZE)))

# while 1:
    # recvData(client.recv(BUFSIZE))

class Wrapper:
	def __init__():
		pass
		
	def run(self):
		pass
		
# def start():
    # for i in xrange(10):
        # client.sendall(sendData('asdfe',1))

# for i in range(10):
    # start_new(start,())
# while 1:
    # # log.msg("connecting server now...")
    # pass
	
if __name__ == '__name__':
	pass

