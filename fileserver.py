import os
import grpc

import click
import logging 

import utils

from concurrent import futures



@click.command()
@click.option("--port", help="Port number")
@click.option("--kind", help="fs: file server or ds: distributed machine")
def start_client(port, kind):
    connection_url = 'localhost:' + port
    channel        = grpc.insecure_channel(connection_url)
    stub           = keyDistServer_pb2_grpc.ConnectStub(channel)
    k              = keyDistServer_pb2.Info(type=kind)
    skey           = stub.ConnectNew(k)

    with open("pass.key", "wb") as key_file:
        key_file.write(str.encode(skey.key))
    
    with open("id.txt", "wb") as id_file:
        id_file.write(str.encode(str(skey.id)))

#TODO: Implement the server to process commands from console
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    pass

if __name__ == "__main__":
    start_file_server()

