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
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./fileserver.proto
```
3. Now we can start the key distribution server, by default on port=51001:
```
python kds.py
```
4. Install the client app using pip
```
pip install .
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

1. getkey : Get the shared key from KDS [Required]

    port = KDS's port
```
client getkey --port=51001
```
2. fileservers : Get information about available fileservers [Required]
    
```
client fileservers
```
3. connect : Connect with the selected fileserver [Required]
    
    id = Fileserver id
```
client --id=1 connect
```
4. upload : Upload a file on the selected file server

    file = path to file
```
client --fs=1 upload --file=./key.txt
```
5. ls : List the contents of directory 
```
client --fs=1 ls
```
6. cp : Copy one file to another
```
client --fs=1 cp --file1=./key.txt --file2=./key2.txt
```
7. cat : Show the contents of a file
```
client --fs=1 cat --file=./key.txt
```
