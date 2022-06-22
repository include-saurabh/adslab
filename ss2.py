import socket, pickle

emplist=(["hari",40000],["ani",50000],["om",60000])
print(emplist)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("127.0.0.1",9096));
serverSocket.listen();

while(True):

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    #dataFromClient = clientConnected.recv(1024)
    #data=dataFromClient.decode()
    #values = ''.join(str(x) for x in emplist)
    #clientConnected.send(values.encode());
    mydata = pickle.dumps(emplist)
    clientConnected.send(mydata);
    #for i in emplist:
     #  for x in i:
      #    clientConnected.send(str(i).encode());
