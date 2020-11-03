import grpc
import crypt
from concurrent import futures
import logging
import keyDistServer_pb2
import keyDistServer_pb2_grpc

from simplecrypt import encrypt, decrypt

from utils import id_generator

def get_Creds(id):
    return keyDistServer_pb2.Creds(key=id_generator(),id=id)


class KeyDistributionServicer(keyDistServer_pb2_grpc.ConnectServicer):

    def __init__(self):
        self.totalFileServers = 0
        self.totalDistMachines = 0
        self.fileServers = {}
        self.distMachines = {}

    def ConnectNew(self, request, context):
        
        if request.type == 'fs':
            print("New file server connected ...")
            print("Sending key and ID...")
            self.totalFileServers+=1
            creds = get_Creds(self.totalFileServers)
            self.fileServers[self.totalFileServers] = creds.key
            print(self.fileServers)
            return creds
        else:
            print("New machine connected ...")
            print("Sending key and ID...")
            self.totalDistMachines+=1
            
            creds = get_Creds(self.totalDistMachines)

            self.distMachines[self.totalDistMachines] = creds.key
            print(self.distMachines)
            return creds

    def Authenticate(self, request, context):
        # crypt.
        # request.message 
        pass
    
    def GetServerInfo(self, request, context):

        pass

        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyDistServer_pb2_grpc.add_ConnectServicer_to_server(
        KeyDistributionServicer(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()