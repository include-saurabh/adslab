print("Enter number of transactions:")
t=int(input())
a=100
b=250
acount=0
bcount=0

print("Value of a:",a)
print("Value of b:",b)
print("***************************")

while(True):
  print("Enter data item:\n1. a\n2. b")
  item=input()
  if item=='a' and acount==0:
    acount=1
  elif item=='b' and bcount==0:
    bcount=1
  else:
   print("Data item is in use")
   print("Stopping Transaction...")
   break
  print("***************************")
  
  print("Enter operation:\n1. Read\n2. Write")
  choice=int(input())
  print("***************************")
  if choice==1 and acount==1:
   print("Value of a:",a)
  elif choice==2 and acount==1:
   print("Performing operation on a...")
   print("New value is:",a+10)
  elif choice==1 and bcount==1:
   print("Value of b:",b)
  elif choice==2 and bcount==1:
   print("Performing operation on b...")
   print("New value is:",b+10)
  else:
   pass
  print("***************************")
  
  print("Release lock:\n1. a\n2. b\n3. Do not release:")
  item2=input()
  if item2=='a':
   acount=0
  if item2=='b':
   bcount=0
  if item2=='3':
   pass
  
  
