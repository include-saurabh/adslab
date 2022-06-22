import socket, pickle

emplist=(["saurabh",10000],["ram",30000],["sham",20000])
print(emplist)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("127.0.0.1",9095));
serverSocket.listen();

while(True):

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    
    mydata = pickle.dumps(emplist)
    clientConnected.send(mydata);
  
