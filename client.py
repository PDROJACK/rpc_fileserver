import socket

import grpc
import keyDistServer_pb2
import keyDistServer_pb2_grpc

import click

import utils

class Client():

    def __init__(self, host = 'localhost', port = '50051')
        self.host = host
        self.port = port
        self.kdcStub = None
        self.availableServers = {}

        connectToServer()

    def connectToServer(self):
        connection_url = self.host +':'+ self.port
        channel        = grpc.insecure_channel(connection_url)
        self.kdcStub   = keyDistServer_pb2_grpc.ConnectStub(channel)
        k              = keyDistServer_pb2.Info(type='ds')
        skey           = self.kdcStub.ConnectNew(k)

        with open("pass.key", "wb") as key_file:
            key_file.write(str.encode(skey.key))
        
        with open("id.txt", "wb") as id_file:
            id_file.write(str.encode(str(skey.id)))

        #TODO: Implement file server information retrieval 
        self.kdcStub
        
        print('Connected successfully...')

    #TODO: Start auth to get nonce and shared key
    def authenticate(self):
        pass

    #TODO: Implement the command execution on console side
    def commands(self):
        pass

if __name__ == "__main__":
