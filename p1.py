print("Enter the number of nodes")
nodes=int(input())
print("****Coordinator Initialized****")
count=0
for i in range (1, nodes+1):
     print("Is node",i, "ready to commit? \n Yes-1 No-0")
     check=int(input())
     if check==1: 
         count=count+1

if count==nodes:
     print("Transaction commited")
else:
     print("Transaction aborted")
