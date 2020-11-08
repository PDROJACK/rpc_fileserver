import socket
import random
import click
import grpc
import pickle
import os

import keyDistServer_pb2
import keyDistServer_pb2_grpc

import fileserver_pb2
import fileserver_pb2_grpc

from simplecrypt import encrypt, decrypt
from configparser import SafeConfigParser,ConfigParser
from utils import JsonToDict, dictToJSON


config = ConfigParser()


class Client(object):

    def __init__(self):
        self.host               = None
        self.port               = None
        self.kdcStub            = None
        self.myKey              = None
        self.myId               = None
        self.fs_stub            = None
        self.availableServers   = {}


pass_client = click.make_pass_decorator(Client, ensure=True)


@click.group()
@click.option('--fs', type=int, help='select file server')
@pass_client
def cli(client, fs):

    if 'main' not in config.sections():
        config.add_section('main')


    if os.path.isfile('./config.ini') == False:
        pass
    else:
        config.read('config.ini')

        client.host               = config['main']['host']
        client.port               = config['main']['port']
        client.myKey              = config['main']['myKey']
        client.myId               = int(config['main']['myId'])

        fileservers = config.sections()
        for i in range(1, len(fileservers)):
            client.availableServers[i] = config[str(fileservers[i])]['url']


        connection_url = config['main']['host'] + ':' + config['main']['port']
        channel        = grpc.insecure_channel(connection_url)
        client.kdcStub = keyDistServer_pb2_grpc.ConnectStub(channel)

        if fs:
            channel        = grpc.insecure_channel(client.availableServers[fs])
            client.fs_stub = fileserver_pb2_grpc.FileServerStub(channel)



@cli.command()
@click.option('--port', help='Port of key distribution server')
@pass_client
def getKey(client, port):
    ''' Connects you with file server or Key distribution server '''

    connection_url = 'localhost:'+ port
    channel        = grpc.insecure_channel(connection_url)
    client.kdcStub = keyDistServer_pb2_grpc.ConnectStub(channel)

    k                     = keyDistServer_pb2.Info(type='ds')
    skey                  = client.kdcStub.ConnectNew(k)
    client.myKey          = skey.key
    client.myId           = skey.id
    
    config.set('main', 'host', 'localhost')
    config.set('main', 'port', port)
    config.set('main', 'myKey', client.myKey)
    config.set('main', 'myId', str(client.myId))
    with open('config.ini', 'w') as configfile:    
        config.write(configfile)

    print('Connected successfully...')


@cli.command()
@click.option('--id', help='ID of fileserver')
@pass_client
def connect(client, id):
    ''' Connects you with file server or Key distribution server '''

    print('Commencing PHASE I of authentication process...')
    nonce   = random.randrange(1000)
    idB     = id
    message = dictToJSON([client.myId, idB, nonce])
    message = encrypt(client.myKey, message)
    res     = client.kdcStub.Authenticate(keyDistServer_pb2.AuthRequestEncrypted(id=client.myId, message=message))
    
    print('PHASE I completed, Received encryted message from KDC...')
    ks, idA, idB, nonce, messageToB = JsonToDict(decrypt(client.myKey, res.message))

    print('Commencing PHASE II sending message to selected file server...')
    print(client.availableServers)
    channel        = grpc.insecure_channel(client.availableServers[(idB)])
    stub           = fileserver_pb2_grpc.FileServerStub(channel)

    encryptedII    = stub.Authenticate(fileserver_pb2.AuthRequest(message=messageToB.encode('latin-1'))).message
    nonceII        = int(decrypt(ks, encryptedII)) + 1

    print('Commencing PHASE II sending nonce to selected file server...')
    finalMessage = encrypt(ks, str(nonceII))
    res = stub.AutheticationComplete(fileserver_pb2.AuthRequest(id=client.myId,message = finalMessage))
    if res.status == 200:
        print('Authentication with file server {} completed successfully'.format(idB))
    else:
        print('Authentication with file server {} failed...'.format(idB))


@cli.command()
@click.option('--file', help='Path of file to upload')
@pass_client
def upload(client,file):
    ''' Enter allowed commands '''
    with open() as f:
        content = f.read()

@cli.command()
@pass_client
def pwd(client):
    ''' Enter allowed commands '''

    command = fileserver_pb2.CommandRequest(command="pwd")
    output = client.fs_stub.TakeCommand(command).output
    output = output.decode('utf-8')
    click.echo(output)

@cli.command()
@pass_client
def ls(client):
    ''' Enter allowed commands '''


@cli.command()
@click.option('--file', help='Path of file to print')
@pass_client
def cat(client, file):
    ''' Enter allowed commands '''


@cli.command()
@pass_client
def fileservers(client):
    ''' Get information about all the connected file servers '''

    infoReq = keyDistServer_pb2.InfoRequest()
    client.availableServers = JsonToDict(client.kdcStub.GetServerInfo(infoReq).file_servers)

    for key, value in client.availableServers.items():
        if not config.has_section(key):
            config.add_section(key)
            config.set(key, 'url', value)
            with open('config.ini', 'w') as configfile:    
                config.write(configfile)

    click.echo(client.availableServers)