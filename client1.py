import socket
import sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1",9095));
data = sys.argv[1];
clientSocket.send(data.encode());
dataFromServer = clientSocket.recv(1024);
print(dataFromServer.decode());
