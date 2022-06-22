import socket, pickle
import sys

clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket1.connect(("127.0.0.1",9095));
def mysort(rdata):
  return(sorted(rdata, key = lambda x: x[1]))


dataFromServer1 = clientSocket1.recv(1024);
rdata1 = pickle.loads(dataFromServer1)


clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket2.connect(("127.0.0.1",9096));
dataFromServer2 = clientSocket2.recv(1024);
rdata2 = pickle.loads(dataFromServer2)


finalmerge=rdata1+rdata2


print(mysort(finalmerge))
