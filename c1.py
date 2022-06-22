import socket
import sys

clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket1.connect(("127.0.0.4",9090));

clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket2.connect(("127.0.0.2",9090));

clientSocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket3.connect(("127.0.0.3",9090));


data = sys.argv[1];

clientSocket1.send(data.encode());
dataFromServer1 = clientSocket1.recv(1024);
print(dataFromServer1.decode());

clientSocket2.send(data.encode());
dataFromServer2 = clientSocket2.recv(1024);
print(dataFromServer2.decode());

clientSocket3.send(data.encode());
dataFromServer3 = clientSocket3.recv(1024);
print(dataFromServer3.decode());
