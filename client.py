import socket
import random
from simplecrypt import encrypt, decrypt
import grpc
import keyDistServer_pb2
import keyDistServer_pb2_grpc

import click

from utils import JsonToDict, dictToJSON

class Client():

    def __init__(self, host = 'localhost', port = '50051'):
        self.host               = host
        self.port               = port
        self.kdcStub            = None
        self.myKey              = None
        self.availableServers   = {}

        self.connectToServer()

        self.authenticate(1)

    def connectToServer(self):
        connection_url = self.host +':'+ self.port
        channel        = grpc.insecure_channel(connection_url)
        self.kdcStub   = keyDistServer_pb2_grpc.ConnectStub(channel)
        k              = keyDistServer_pb2.Info(type='ds')
        skey           = self.kdcStub.ConnectNew(k)
        self.myKey     = skey.key
        self.myId      = skey.id

        with open("pass.key", "wb") as key_file:
            key_file.write(str.encode(skey.key))
        
        with open("id.txt", "wb") as id_file:
            id_file.write(str.encode(str(skey.id)))

        infoReq = keyDistServer_pb2.InfoRequest()

        self.availableServers = JsonToDict(self.kdcStub.GetServerInfo(infoReq).file_servers)
        
        print('Connected successfully...')

    ## IdB is parameter
    def authenticate(self, idB):
        print('Commencing PHASE I of authentication process...')
        nonce = random.randrange(1000)
        message = dictToJSON([self.myId, idB, nonce])
        message = encrypt(self.myKey, message)
        #print(message.decode("utf-8"))
        res = self.kdcStub.Authenticate(keyDistServer_pb2.AuthRequestEncrypted(id=self.myId, message=message))
        
        print('PHASE I completed, Received encryted message from KDC...')
        ks, idA, idB, nonce, messageToB = JsonToDict(decrypt(self.myKey, res.message))

        #TODO: Implement ticket to Fileserver rpc method here 
        
        print('Commencing PHASE II sending message to selected  file server...')



    #TODO: Implement the command execution on console side
    def commands(self):
        
        pass

if __name__ == "__main__":
    client = Client()