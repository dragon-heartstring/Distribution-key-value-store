import json
import os
from kazoo.client import KazooClient,KazooState
from socket import *
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
port_list=[]
lis_mixed=[]
list_mixed=[]
name_list=[]
i=[]
if zk.exists("/zlist") :
	zk.set("/zlist","12000 /masternode 12345 /alphanode 65000 /numnode 45678 /alphanode1 45876 /specnode")
	check_lis=zk.get("/zlist")
	check_list=check_lis[0]
	lis_mixed=check_list.split(" ")
for i in range (0,len(lis_mixed),2) :
	port_list.append(int(lis_mixed[i]))

for j in range (1,len(lis_mixed),2) :
	name_list.append(str(lis_mixed[j]))

i= str(str(port_list[0])+" "+name_list[0])
zk.create(name_list[0],i, ephemeral=True)
#print(zk.get("/masternode"))

if zk.exists("/bklist") :
	zk.set("/bklist","12000 /masternode 65000 /numnode 45678 /alphanode1 45876 /specnode 12345 /alphanode")
	check_lis=zk.get("/bklist")
	check_list=check_lis[0]
	list_mixed=check_list.split(" ") 

master=1
serverPort=port_list[0]
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)
changed=" "
print("I am the master server! My job is to send the list of port numbers and respective nodes to the client!")
print("If I stop working...any of the other servers can take my place!\n")
while 1:
	
	connectionSocket, addr = serverSocket.accept()
	changed=connectionSocket.recv(4096)
	if changed=="~!<>" :
		connectionSocket.send(str(lis_mixed))
		print("List of port number have been sent!\n")
		connectionSocket.close()
	connectionSocket, addr = serverSocket.accept()
	connectionSocket.recv(4096)
	connectionSocket.send(str(list_mixed))
	print ("Just sent back up port number and name to the client")
	connectionSocket.close()
	
	
	


connectionSocket.close()







