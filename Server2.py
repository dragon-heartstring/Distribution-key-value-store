from kazoo.client import KazooClient,KazooState
from socket import *
import sys
import json
import os
import ast
import time
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
print "Hi! I am server responsible for keys beginning with 'a' and going on till 'o'"
print "I can be the master if the master server dies!" 
string=""
while 1 :
	set1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
	alphadict1={"@": "atr" , "?":"qm" , "#":"hash" ,"$":"dollar" , "%":"perc"}
	alphadict={"a": "apple" , "b":"ball" , "c":"cat" ,"d":"dog" , "m":"mango"}
	store=[]	
	from socket import *
	serverPort = 12345
	serverSocket = socket(AF_INET,SOCK_STREAM) 
	serverSocket.bind(('',serverPort)) 
	serverSocket.listen(1)
	temp_var1=[]
	port_list=[]
	name_list=[]
	port_list1=[]
	name_list1=[]
	lis_mixed=[]
	list_mixed=[]
	change=" "
	bk_dict={}
	while zk.exists("/masternode") or zk.exists("/masternode1") :
		if zk.exists("/alphanode") :
			zk.set("/alphanode","12345 alpha")
			
		else :	
			zk.create("/alphanode", "12345 alpha", ephemeral=True)
			if zk.exists("/zalpha") and change==" " :
				t=zk.get("/zalpha")
				bk_dict=ast.literal_eval(t[0])
				change="!!!"
				if len(bk_dict)>=len(alphadict):
					alphadict=bk_dict 
					print(alphadict)
				else :
					pass
	
		connectionSocket, addr = serverSocket.accept() 
		temp_variable = connectionSocket.recv(2048) 
		if temp_variable[0].isalpha() and temp_variable[0] in set1 :
			temp_var1=temp_variable.split(" ")
			if (temp_var1[0] not in alphadict.keys()) or (temp_var1[0] in alphadict.keys() and temp_var1[1]!=alphadict[temp_var1[0]]) :
				if temp_var1[1]=="null" : 
					if temp_var[0] in alphadict :
						key1=str(temp_var1[0])
						value=alphadict[key1]
						print (value) 
						connectionSocket.send(value) 
						connectionSocket.close()
					else :
						connectionSocket.send("Key doesn't exist in the dictionary!")
				else :
					alphadict[temp_var1[0]]=temp_var1[1]
					print (alphadict)
					connectionSocket.send("the store has been updated")
					connectionSocket.close()
					time.sleep(5)
					if zk.exists("/numnode") :
						clientSocket = socket(AF_INET, SOCK_STREAM)
						t=zk.get("/numnode")
						store=t[0].split(" ")
						back_num=int(store[0])
						clientSocket.connect(("0.0.0.0",back_num))
						clientSocket.send(temp_variable)
						clientSocket.close()
						

					elif zk.exists("/masternode1") :
						t=zk.get("/masternode1")
						clientSocket = socket(AF_INET, SOCK_STREAM)
						store=t[0].split(" ")
						back_num=int(store[0])
						clientSocket.connect(("0.0.0.0",back_num))
						clientSocket.send(temp_variable)
						clientSocket.close()

					else :
						pass
			else :
				connectionSocket.close()
						

		elif temp_variable[0] in ['!','@','#','$','%','^','&','*','(',')','`']  :
			temp_var1=temp_variable.split(" ")
			if temp_var1[1]=="null" :
				key1=str(temp_var1[0])
				value=alphadict1[key1]
				print (value) 
				connectionSocket.send(value) 
				connectionSocket.close()
				
	
			elif (temp_var1[0] not in alphadict1.keys()) or (temp_var1[0] in alphadict1.keys() and temp_var1[1]!=alphadict1[temp_var1[0]]):
				alphadict1[temp_var1[0]]=temp_var1[1]
				if zk.exists("/zspec"):
					zk.set("/zspec",str(alphadict1))
				print(alphadict1)
				connectionSocket.send("the store has been updated")
				connectionSocket.close()
				time.sleep(5)
				if zk.exists("/specnode") :
					t=zk.get("/specnode")
					store=t[0].split(" ")
					back_num=int(store[0])
					for key in alphadict1 :
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(('0.0.0.0',back_num))
						next_temp=str(key)+" "+str(alphadict1[key])
						clientSocket.send(next_temp)
						clientSocket.close()
					
				elif zk.exists("/masternode1") :
					t=zk.get("/masternode1")
					store=t[0].split(" ")
					back_num=int(store[0])
					for key in alphadict1 :
						clientSocket = socket(AF_INET, SOCK_STREAM)
						clientSocket.connect(('0.0.0.0',back_num))
						next_temp=str(key)+" "+str(alphadict1[key])
						clientSocket.send(next_temp)
						clientSocket.close()

					

				else :
					pass

			else :
				connectionSocket.close()

		else :
			connectionSocket.close()

		zk.delete("/alphanode")
		

	else :
		print("I might become the master!")
		time.sleep(2)
		if zk.exists("/masternode1") :
			print("Someone else became the master so I can't! Going back to my regular duties")
			os.system("gnome-terminal -e 'python Server2.py'")
			quit()
		else :
			print 'I have become the master! I am ready to receive!I will carry out my regular duties and master duties!\n'

			if zk.exists("/zlist") :
				zk.set("/zlist","12000 /masternode 12000 /masternode1 65000 /numnode 45678 /alphanode1 45876 /specnode")	
				check_lis=zk.get("/zlist")
			check_list=check_lis[0]
			lis_mixed=check_list.split(" ")
			for i in range (0,len(lis_mixed),2) :
				port_list.append(int(lis_mixed[i]))

			for j in range (1,len(lis_mixed),2) :
				name_list.append(str(lis_mixed[j]))

			i= str(str(port_list[1])+" "+name_list[1])
			zk.create(name_list[1],i, ephemeral=True)
			serverSocket = socket(AF_INET,SOCK_STREAM) 
			serverSocket.bind(('',port_list[1])) 
			serverSocket.listen(1)
			
			if zk.exists("/bklist") :
				zk.set("/bklist","12000 /masternode 65000 /numnode 45678 /alphanode1 45876 /specnode 12000 /masternode1")
				check_lis=zk.get("/bklist")
			check_list=check_lis[0]
			list_mixed=check_list.split(" ") 
			
			while 1 :
				if zk.exists("/zalpha") and change==" " :
					t=zk.get("/zalpha")
					bk_dict=ast.literal_eval(t[0])
					change="!!!"
					if len(bk_dict)>=len(alphadict):
						alphadict=bk_dict 
						print(alphadict)
				else :
					pass
				connectionSocket, addr = serverSocket.accept() 
				temp_variable = connectionSocket.recv(4096) 
				if temp_variable[0].isalpha() and temp_variable[0] in set1 :
					temp_var1=temp_variable.split(" ")
					if (temp_var1[0] not in alphadict.keys()) or (temp_var1[0] in alphadict.keys() and temp_var1[1]!=alphadict[temp_var1[0]]) :
						if temp_var1[1]=="null" :
							key1=str(temp_var1[0])
							value=alphadict[key1]
							print (value) 
							connectionSocket.send(value) 
							connectionSocket.close()

						else :
							alphadict[temp_var1[0]]=temp_var1[1]
							print (alphadict)
							connectionSocket.send("the store has been updated")
							connectionSocket.close()
							if zk.exists("/numnode") :
								clientSocket = socket(AF_INET, SOCK_STREAM)
								t=zk.get("/numnode")
								store=t[0].split(" ")
								back_num=int(store[0])
								clientSocket.connect(("0.0.0.0",back_num))
								clientSocket.send(temp_variable)
								clientSocket.close()
							else :
								pass	
					else :
						connectionSocket.close()
								

				elif temp_variable[0] in ['!','@','#','$','%','^','&','*','(',')','`'] :
					temp_var1=temp_variable.split(" ")
					if temp_var1[1]=="null" :
						key1=str(temp_var1[0])
						value=alphadict1[key1]
						print (value) 
						connectionSocket.send(value) 
						connectionSocket.close()	
					elif (temp_var1[0] not in alphadict1.keys()) or (temp_var1[0] in alphadict1.keys() and temp_var1[1]!=alphadict1[temp_var1[0]]):
						alphadict1[temp_var1[0]]=temp_var1[1] 
						if zk.exists("/zspec"):
							zk.set("/zspec",str(alphadict1))
						print(alphadict1)
						connectionSocket.send("the store has been updated")
						connectionSocket.close()
						if zk.exists("/specnode") :
							t=zk.get("/specnode")
							store=t[0].split(" ")
							back_num=int(store[0])
							for key in alphadict1 :
								clientSocket = socket(AF_INET, SOCK_STREAM)
								clientSocket.connect(('0.0.0.0',back_num))
								next_temp=str(key)+" "+str(alphadict1[key])
								clientSocket.send(next_temp)
								clientSocket.close()
						else :
							pass

					else :
						connectionSocket.close()


				elif (temp_variable=="~!<>") :
					connectionSocket.send(str(lis_mixed))
					print("Just sent a list of port numbers and their respective names!")
					connectionSocket.close()
			
				elif (temp_variable[0].isdigit())or (temp_variable[0].isalpha() and temp_variable[0] not in set1) :
					connectionSocket.send(str(list_mixed))
					print("Just sent a back up list of port numbers and their respective names!")
					print("Looks like a server is down or has changed it's name! Me to the rescue!")
					connectionSocket.close()

				else:
					connectionSocket.send("Error! \n")
					connectionSocket.close()


	 
		

