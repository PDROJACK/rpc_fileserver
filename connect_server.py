import grpc
import crypt
from concurrent import futures
import logging
import keyDistServer_pb2
import keyDistServer_pb2_grpc

from simplecrypt import encrypt, decrypt

from utils import id_generator, dictToJSON

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
            return creds

    #TODO: Start Authentication from console to Kdc to server cycle
    def Authenticate(self, request, context):
        # crypt.
        # request.message 
        pass
    
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
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()