import socket

import grpc
import keyDistServer_pb2
import keyDistServer_pb2_grpc

import click

import utils

# HOST = '127.0.0.1'
# PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'data')
#     data = s.recv(1024)

# print('Received', repr(data))

@click.command()
@click.option("--port", help="Port number")
@click.option("--kind", help="fs: file server or ds: distributed machine")
def start_client(port, kind):
    connection_url = 'localhost:' + port
    channel = grpc.insecure_channel(connection_url)
    stub = keyDistServer_pb2_grpc.ConnectStub(channel)
    k = keyDistServer_pb2.Info(type=kind)
    skey = stub.ConnectNew(k)

    with open("pass.key", "wb") as key_file:
        key_file.write(str.encode(skey.key))
    
    with open("id.txt", "wb") as id_file:
        id_file.write(str.encode(str(skey.id)))


if __name__ == "__main__":
    start_client()
