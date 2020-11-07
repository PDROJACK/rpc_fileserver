import grpc
import crypt
from concurrent import futures
import logging
import keyDistServer_pb2
import keyDistServer_pb2_grpc

from simplecrypt import encrypt, decrypt

from utils import id_generator, dictToJSON, JsonToDict

def get_Creds(id):
    return keyDistServer_pb2.Creds(key=id_generator(),id=id)


class KeyDistributionServicer(keyDistServer_pb2_grpc.ConnectServicer):

    def __init__(self):
        self.totalFileServers   = 0
        self.totalDistMachines  = 0
        self.fileServers        = {}
        self.distMachines       = {}

    def ConnectNew(self, request, context):
        if request.type == 'fs':
            print("New file server connected ...")
            print("Sending key and ID...")
            self.totalFileServers+=1
            creds = get_Creds(self.totalFileServers)
            self.fileServers[self.totalFileServers] = (creds.key, request.url)
            #print(self.fileServers)
            return creds
        else:
            print("New machine connected ...")
            print("Sending key and ID...")
            self.totalDistMachines+=1
            creds = get_Creds(self.totalDistMachines)
            self.distMachines[self.totalDistMachines] = creds.key
            print(self.distMachines)
            return creds

    #TODO: Start Authentication from console to Kdc to server cycle
    def Authenticate(self, request, context):

        print('Receiving encrypted transmission...')

        idA = int(request.id)

        print('Deciphering encrypted transmission...')
        print(self.distMachines)
        decrypted = JsonToDict(decrypt(self.distMachines[idA] , request.message ))
        idB = int(decrypted[1])
        nonce = decrypted[2]
        ks = id_generator()

        ticket = encrypt( self.fileServers[idB][0] , dictToJSON([idA, ks]))
        message = encrypt( self.distMachines[idA] , dictToJSON([ks, idA, idB, nonce, ticket.decode('latin-1')]))

        print('Sending new encrypted transmission back...')

        return keyDistServer_pb2.AuthResponse(message = message)
    
    def GetServerInfo(self, request, context):
        res = {}
        for key, value in self.fileServers.items():
            res[key] = value[1]

        info = dictToJSON(res)
        res = keyDistServer_pb2.InfoResponse(file_servers = info)
        return res

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyDistServer_pb2_grpc.add_ConnectServicer_to_server(
        KeyDistributionServicer(),
        server
    )
    port = 51001
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    print('KD server running on port {}'.format(port))
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()