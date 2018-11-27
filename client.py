from kazoo.client import KazooClient,KazooState
import sys
import os
import json
import ast
from socket import *

import os
tup=" "
cre=[]
zk = KazooClient(hosts='127.0.0.1:2181')
t=[]
mixed1=[]
print("Hi! Welcome to our distribution store!")
print("Our keys are mapped across four different servers")
print("Our first server maps keys that begin with a-o/A-O")
print("Our second server maps keys that begin with digits")
print("Our third server maps keys that begin with p-z/P-Z")
print("Our fourth server maps keys that begin with special characters.")
print("The get and put requests are handled by our servers")
print("If you wish to retrieve a value for a key then leave the value coloumn empty")
print("If you wish to enter key-value pair then enter values for keys and values")
print("We have managed to handle most of the error cases \n")

set1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
set2=['p','q','r','s','t','u','v','w','x','y','z']
def my_listener(state):
	if state==KazooState.LOST:
		print("lost")
	elif state==KazooState.SUSPENDED:
		print("suspended")
	else:
		print("Connected to the zookeeper...trying to establish connection with the master...\n")

zk.add_listener(my_listener)
zk.start()
if zk.exists("/masternode"):
	t=zk.get("/masternode")

elif zk.exists("/masternode1") :
	t=zk.get("/masternode1")
else :
	print("The master is not ready yet!")
	print("Try again later!")
	quit()

#print(t[0])
lis=[]	
port_list=[]
name_list=[]
port_list1=[]
name_list1=[]
list_mixed=[]
x=t[0]
lis=x.split(' ') 
port=lis[0]
port1=int(port)
name=lis[1] 
changed= " " 

print("The port number connected to : %s" %(port1))
print("The server the client is connected to : %s"%(lis[1]))

while 1 :
	if(changed==" ") :
		clientSocket = socket(AF_INET, SOCK_STREAM) 
		clientSocket.connect(("0.0.0.0",port1))
		clientSocket.send("~!<>")
		changed=clientSocket.recv(4096)
		clientSocket.close()

	changed1 = ast.literal_eval(changed) 		

	for i in range(0,len(changed1),2):
		port_list.append(changed1[i])
	for i in range(1,len(changed1),2):
		name_list.append(changed1[i])
	
	key=" "
	value=" "
	key=raw_input("Enter key value: ")
	value=raw_input("Enter value value: ")
	if value==" " :
		value="null"

	final_variable=key+" "+value
	
	if key[0].isalpha() :
		chan=key.lower()
		key1=list(chan)
		if chan[0] in set1 :			
			if zk.exists(name_list[1]) :
				t1=zk.get(name_list[1])
				x=t1[0]
				lis1=x.split(' ')
				port=int(lis1[0])
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port))
				clientSocket.send(final_variable)
				val=clientSocket.recv(4096)
				clientSocket.close()
				print(val)
				
			else :
				if zk.exists("/masternode") :
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port1))
					clientSocket.send("~!><")
					mixed=clientSocket.recv(4096)		
					clientSocket.close()
					mixed1=ast.literal_eval(mixed)
					for i in range(0,len(mixed1),2):
						port_list1.append(mixed1[i])
					for i in range(1,len(mixed1),2):
						name_list1.append(mixed1[i])
					if zk.exists(name_list1[1]) :
						t1=zk.get(name_list1[1])
						x=t1[0]
						lis1=x.split(' ')
						port=int(lis1[0])
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(("0.0.0.0",port))
						clientSocket.send(final_variable)
						val=clientSocket.recv(4096)
						clientSocket.close()
		                                print(val)

				elif zk.exists("/masternode1") :
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port1))
					clientSocket.send(final_variable)
					mixed=clientSocket.recv(4096)  
					clientSocket.close()
					if mixed[0]=="[" :
						print("i reached here")
						mixed1=ast.literal_eval(mixed)
						for i in range(0,len(mixed1),2):
							port_list1.append(mixed1[i])
						for i in range(1,len(mixed1),2):
							name_list1.append(mixed1[i])
						if zk.exists(name_list1[1]) :
							t1=zk.get(name_list1[1])
							x=t1[0]
							lis1=x.split(' ')
							port=int(lis1[0])
							name=str(lis1[1])
							print (port)
							print (name)
							clientSocket = socket(AF_INET, SOCK_STREAM)
							clientSocket.connect(("0.0.0.0",port))
							clientSocket.send(final_variable)
							val=clientSocket.recv(4096)
							clientSocket.close()
							print(val)
					else :
						print(mixed)
				else :
					print("The distribution store cannot accept this key value pair right now!")
					print("Please try another key value pair or try the same pair in sometime!")
					
					
				
		else :
			if zk.exists(name_list[3]) :
				t1=zk.get(name_list[3])
				x=t1[0]
				lis1=x.split(' ')
				port=int(lis1[0])
				name=str(lis1[1])
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port))
				clientSocket.send(final_variable)
				val=clientSocket.recv(4096)
				clientSocket.close()
				print(val)
				
			else :
				if zk.exists("/masternode") :
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port1))
					clientSocket.send("~!><")
					mixed=clientSocket.recv(4096)
					clientSocket.close()
					mixed1=ast.literal_eval(mixed)
					for i in range(0,len(mixed1),2):
						port_list1.append(mixed1[i])
					for i in range(1,len(mixed1),2):
						name_list1.append(mixed1[i])
					if zk.exists(name_list1[3]) :
						t1=zk.get(name_list1[3])
						x=t1[0]
						lis1=x.split(' ')
						port=int(lis1[0])
						name=str(lis1[1])
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(("0.0.0.0",port))
						clientSocket.send(final_variable)
						val=clientSocket.recv(4096)
						clientSocket.close()
						print(val)

				elif zk.exists("/masternode1") :
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port1))
					clientSocket.send(final_variable)
					mixed=clientSocket.recv(4096)  
					clientSocket.close()
					if mixed[0]=="[" :
						mixed1=ast.literal_eval(mixed)
						for i in range(0,len(mixed1),2):
							port_list1.append(mixed1[i])
						for i in range(1,len(mixed1),2):
							name_list1.append(mixed1[i])
						if zk.exists(name_list1[3]) :
							t1=zk.get(name_list1[3])
							x=t1[0]
							lis1=x.split(' ')
							port=int(lis1[0])
							name=str(lis1[1])
							clientSocket = socket(AF_INET, SOCK_STREAM)
							clientSocket.connect(("0.0.0.0",port))
							clientSocket.send(final_variable)
							val=clientSocket.recv(4096)
							clientSocket.close()
							print(val)
					else :
						print(mixed)	
				else :
						
					print("The distribution store cannot accept this key value pair right now!")
					print("Please try another key value pair or try the same pair in sometime!")
										
				
	elif key[0].isdigit() :
		if zk.exists(name_list[2]):
			t1=zk.get(name_list[2])
			x=t1[0]
			lis1=x.split(' ')
	 	 	port=int(lis1[0])
			name=str(lis1[1])
			clientSocket = socket(AF_INET, SOCK_STREAM)
			clientSocket.connect(("0.0.0.0",port))
			clientSocket.send(final_variable)
			val=clientSocket.recv(4096)
			clientSocket.close()
			print(val)
		else :
			if zk.exists("/masternode"): 
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port1))
				clientSocket.send("~!><")
				mixed=clientSocket.recv(4096)
				clientSocket.close()
				mixed1=ast.literal_eval(mixed)
				for i in range(0,len(mixed1),2):
					port_list1.append(mixed1[i])
				for i in range(1,len(mixed1),2):
					name_list1.append(mixed1[i])
				if zk.exists(name_list1[2]) :
					t1=zk.get(name_list1[2])
					x=t1[0]
					lis1=x.split(' ')
					port=int(lis1[0])
					name=str(lis1[1])
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port))
					clientSocket.send(final_variable)
					val=clientSocket.recv(4096)
					clientSocket.close()
					print(val)

			elif zk.exists("/masternode1") :
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port1))
				clientSocket.send(final_variable)
				mixed=clientSocket.recv(4096)  
				clientSocket.close()
				if mixed[0]=="[" :
					mixed1=ast.literal_eval(mixed)
					for i in range(0,len(mixed1),2):
						port_list1.append(mixed1[i])
					for i in range(1,len(mixed1),2):
						name_list1.append(mixed1[i])
					if zk.exists(name_list1[2]) :
						t1=zk.get(name_list1[2])
						x=t1[0]
						lis1=x.split(' ')
						port=int(lis1[0])
						name=str(lis1[1])
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(("0.0.0.0",port))
						clientSocket.send(final_variable)
						val=clientSocket.recv(4096)
						clientSocket.close()
						print(val)
					else :
						print(mixed)
			else :
				print("The distribution store cannot accept this key value pair right now!")
				print("Please try another key value pair or try the same pair in sometime!")
				
	elif key[0] in ['!','@','#','$','%','^','&','*','(',')','`'] :
		if zk.exists(name_list[4]):
			t1=zk.get(name_list[4])
			x=t1[0]
			lis1=x.split(' ')
	 	 	port=int(lis1[0])
			name=str(lis1[1])
			clientSocket = socket(AF_INET, SOCK_STREAM)
			clientSocket.connect(("0.0.0.0",port))
			clientSocket.send(final_variable)
			val=clientSocket.recv(4096)
			clientSocket.close()
			print(val)
		else :
			if zk.exists("/masternode") :
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port1))
				clientSocket.send("~!><")
				mixed=clientSocket.recv(4096)  
				clientSocket.close()
				mixed1=ast.literal_eval(mixed)
				for i in range(0,len(mixed1),2):
					port_list1.append(mixed1[i])
				for i in range(1,len(mixed1),2):
					name_list1.append(mixed1[i])
				if zk.exists(name_list1[4]) :
					t1=zk.get(name_list1[4])
					x=t1[0]
					lis1=x.split(' ')
					port=int(lis1[0])
					name=str(lis1[1])
					clientSocket = socket(AF_INET, SOCK_STREAM)
					clientSocket.connect(("0.0.0.0",port))
					clientSocket.send(final_variable)
					val=clientSocket.recv(4096)
					clientSocket.close()
					print(val)

			elif zk.exists("/masternode1") :
				clientSocket = socket(AF_INET, SOCK_STREAM)
				clientSocket.connect(("0.0.0.0",port1))
				clientSocket.send(final_variable)
				mixed=clientSocket.recv(4096)  
				clientSocket.close()
				if mixed[0]=="[" :
					mixed1=ast.literal_eval(mixed)
					for i in range(0,len(mixed1),2):
						port_list1.append(mixed1[i])
					for i in range(1,len(mixed1),2):
						name_list1.append(mixed1[i])
					if zk.exists(name_list1[4]) :
						t1=zk.get(name_list1[4])
						x=t1[0]
						lis1=x.split(' ')
						port=int(lis1[0])
						name=str(lis1[1])
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(("0.0.0.0",port))
						clientSocket.send(final_variable)
						val=clientSocket.recv(4096)
						clientSocket.close()
						print(val)
				else :
					print(mixed)
			else :
				print("The distribution store cannot accept this key value pair right now!")
				print("Please try another key value pair or try the same pair in sometime!")

	elif (key=="exit" and value=="null") :
		quit()
	
	else :
		print("There is no provision for this particular key! Please try again with another key-value pair!")

	print ('%s'%(port)+"	"+'%s'%(name))

	
try:
	zk = KazooClient(hosts='127.0.0.1:2181')
	zk.start()

except:
	pass


	


