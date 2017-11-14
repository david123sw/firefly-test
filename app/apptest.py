#coding:utf8

from firefly.server.globalobject import netserviceHandle
from firefly.server.globalobject import GlobalObject
from datetime import *
from twisted.python import log

def doConnectionMade(conn):
    log.msg('custom login echo')
    
def doConnectionLost(conn):
    log.msg('custom logoff echo')
    
GlobalObject().netfactory.doConnectionMade = doConnectionMade
GlobalObject().netfactory.doConnectionLost = doConnectionLost

# @netserviceHandle
# def echo_1(_conn,data):
#	GlobalObject().netfactory.pushObject(1000, '', [])
#	GlobalObject().netfactory.connmanager._connections.keys()
    # return data
    
@netserviceHandle
def act_1000(_conn, data):
    log.msg('act_1000 call:', str(_conn.transport.sessionno))
    log.msg('Data from client:', data)
    
@netserviceHandle
def act_1001(_conn, data):
    log.msg('act_1001 call:', str(_conn.transport.sessionno))
    log.msg('Data from client:', data)
    


    


