## rpc_fileserver

KDS: Key Distribution Server

A Distributed file server with Needham-Schroeder based authentication built using gRPC, accompanied by a command line client app to control the selected file server on the distributed network.

Follow the steps carefully:

1. First we have to install python requirements:
```
pip install -r requirements.txt
```
2. Then we have to compile the .proto files, run these commands:
```
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./keyDistServer.proto
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./keyDistServer.proto
```
3. Now we can start the key distribution server, by default on port=51001:
```
python connect_server.py
```

Now our key distributions server is ready to distribute keys to file servers and clients

Start and authenticate a fileserver, here port is our port and kport is key dist. servers port
```
python fileserver.py --port=50001 --kport=51001
```

Start and authenticate a client, here port is KDS's port
```
client getkey --port=51001
```

A client is a separate command line program using which we can use to store, move, copy and view files in fileservers. Below is the list of commands and their examples:

[WORK IN PROGRESS]