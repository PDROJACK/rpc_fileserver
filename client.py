import socket

import grpc
import keyDistServer_pb2
import keyDistServer_pb2_grpc

import click

from utils import JsonToDict

class Client():

    def __init__(self, host = 'localhost', port = '50051'):
        self.host               = host
        self.port               = port
        self.kdcStub            = None
        self.myKey              = None
        self.availableServers   = {}

        self.connectToServer()

    def connectToServer(self):
        connection_url = self.host +':'+ self.port
        channel        = grpc.insecure_channel(connection_url)
        self.kdcStub   = keyDistServer_pb2_grpc.ConnectStub(channel)
        k              = keyDistServer_pb2.Info(type='fs')
        self.myKey     = self.kdcStub.ConnectNew(k)

        with open("pass.key", "wb") as key_file:
            key_file.write(str.encode(skey.key))
        
        with open("id.txt", "wb") as id_file:
            id_file.write(str.encode(str(skey.id)))

        #TODO: Implement file server information retrieval 
        infoReq = keyDistServer_pb2.InfoRequest()

        self.availableServers = JsonToDict(self.kdcStub.GetServerInfo(infoReq).file_servers)
        
        print('Connected successfully...')

    #TODO: Start auth to get nonce and shared key
    def authenticate(self):
        pass

    #TODO: Implement the command execution on console side
    def commands(self):
        pass

if __name__ == "__main__":
    client = Client()