import socket
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="saurabh",
  password="pass",
  database="testdb"
)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("127.0.0.4",9090));
serverSocket.listen();
while(True):

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    dataFromClient = clientConnected.recv(1024)
    mycursor = mydb.cursor()
    mycursor.execute(dataFromClient.decode())
    myresult = mycursor.fetchall()
    values = ''.join(str(x) for x in myresult)
    clientConnected.send(values.encode());
    
