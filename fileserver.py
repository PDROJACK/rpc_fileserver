import os
import grpc
import random
import click
import logging 
from simplecrypt import encrypt, decrypt
import utils
import fileserver_pb2
import fileserver_pb2_grpc
import subprocess

import keyDistServer_pb2
import keyDistServer_pb2_grpc

from concurrent import futures

from utils import JsonToDict, dictToJSON
import random

class FileServerServicer(fileserver_pb2_grpc.FileServerServicer):

    def __init__(self, myKey = None, myId = None):
        self.connectedTerminals = {}
        self.myKey = myKey
        self.myId = myId

    ##TODO: Phase II of authentication
    def Authenticate(self, request, response):
        try:
            idA, ks = JsonToDict(decrypt(self.myKey, request.message))
            nonce = random.randrange(1000)
            self.connectedTerminals[idA] = [ks, nonce, False]

            message = encrypt(ks, str(nonce))
            return keyDistServer_pb2.AuthResponse(message=message)
        except:
            ## TODO: execute rollback
            pass


    def AutheticationComplete(self, request, response):
        try:

            # print(request)

            ks, nonce, state = self.connectedTerminals[request.id]
            #print(self.connectedTerminals[request.id])
            received_nonce = decrypt(ks, request.message)
            received_nonce = int(received_nonce.decode('latin-1'))
            print(received_nonce)
            if (received_nonce - 1) == nonce:
                print('Terminal conncected..')
                self.connectedTerminals[request.id] = [ks, nonce, True]
                return keyDistServer_pb2.AuthResponse(status=200)
            else:
                print('Terminal connection failed..')
                return keyDistServer_pb2.AuthResponse(status=400)
            
        except:
            pass
            ##TODO: execute rollback
        

    #TODO: Implement the server to process commands from console
    def TakeCommand(self, request, response):
        
        command = request.command
        print(command)
        if command == 'pwd':
            
            return fileserver_pb2.CommandResponse(output = subprocess.check_output('pwd'))


@click.command()
@click.option("--kport", help="KDC Port number")
@click.option("--port", help="Port to run the fileserver")
def serve(port, kport):
    connection_url = 'localhost:' + kport
    my_url         = 'localhost:' + port
    channel        = grpc.insecure_channel(connection_url)
    stub           = keyDistServer_pb2_grpc.ConnectStub(channel)
    k              = keyDistServer_pb2.Info(type='fs', url=my_url)
    skey           = stub.ConnectNew(k)

    with open("pass.key", "wb") as key_file:
        key_file.write(str.encode(skey.key))
    
    with open("id.txt", "wb") as id_file:
        id_file.write(str.encode(str(skey.id)))
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fileserver_pb2_grpc.add_FileServerServicer_to_server(
        FileServerServicer(myKey=skey.key, myId=skey.id),
        server
    )
    server.add_insecure_port(my_url)
    server.start()
    print('File server running on port {}'.format(port))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

