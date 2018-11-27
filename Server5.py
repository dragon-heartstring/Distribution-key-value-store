from kazoo.client import KazooClient,KazooState
from socket import *
import time
import sys
import json
import ast
import os
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

print "Hi! I am server responsible for keys starting with special characters!"
print "I can be the master if the master server dies!" 
while 1:
	store=[]
	set2=['p','q','r','s','t','u','v','w','x','y','z']
	alphadict1={"p": "parrot" , "q":"question" , "r":"rabbit" ,"s":"saiyonara" , "z":"zebra"}
	alphadict={"@": "atr" , "?":"qm" , "#":"hash" ,"$":"dollar" , "%":"perc"}	
	from socket import *
	serverPort = 45786
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
		if zk.exists("/specnode") :
			zk.set("/specnode","45786 special")
		else :	
			zk.create("/specnode", "45786 special", ephemeral=True)
			if zk.exists("/zspec") and change==" " :
				t=zk.get("/zspec")
				bk_dict=ast.literal_eval(t[0])
				change="!!!"
				if len(bk_dict)>=len(alphadict):
					alphadict=bk_dict 
					print(alphadict)
				else :
					pass

		connectionSocket, addr = serverSocket.accept() 
		temp_variable = connectionSocket.recv(2048) 
		if temp_variable[0] in ['!','@','#','$','%','^','&','*','(',')','`'] :
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
					time.sleep(5)
					if zk.exists("/alphanode") :
						clientSocket = socket(AF_INET, SOCK_STREAM)
						t=zk.get("/alphanode")
						store=t[0].split(" ")
						back_num=int(store[0])
						clientSocket.connect(("0.0.0.0",back_num))
						clientSocket.send(temp_variable)
						clientSocket.close()
					elif zk.exists("/masternode1") :
						clientSocket = socket(AF_INET, SOCK_STREAM)
						t=zk.get("/masternode1")
						store=t[0].split(" ")
						back_num=int(store[0])
						clientSocket.connect(("0.0.0.0",back_num))
						clientSocket.send(temp_variable)
						clientSocket.close()
					
					else :
						pass
			else :
				pass
					

		elif temp_variable[0].isalpha() and temp_variable[0] in set2 :
			temp_var1=temp_variable.split(" ")
			if temp_var1[1]=="null" :
				key1=str(temp_var1[0])
				value=alphadict1[key1]
				print (value) 
				connectionSocket.send(value) 
				connectionSocket.close()	
			elif (temp_var1[0] not in alphadict1.keys()) or (temp_var1[0] in alphadict1.keys() and temp_var1[1]!=alphadict1[temp_var1[0]]):
				alphadict1[temp_var1[0]]=temp_var1[1]
				if zk.exists("/zalpha1"):
					zk.set("/zalpha1",str(alphadict1))
				print(alphadict1)
				connectionSocket.send("the store has been updated")
				connectionSocket.close()
				time.sleep(5)
				if zk.exists("/alphanode1") :
					t=zk.get("/alphanode1")
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
				pass

		else :
			pass

		zk.delete("/specnode")
	else :
		print("I might become the master!\n")
		time.sleep(8)
		if zk.exists("/masternode1") :
			print("I have entered here!")
			os.system("gnome-terminal -e 'python Server5.py'")
			quit()
		else :
			print 'I have become the master!I am ready to receive!\n'
			if zk.exists("/zlist") :
				zk.set("/zlist","12000 /masternode 12345 /alphanode 65000 /numnode 45678 /alphanode1 12000 /masternode1")	
				check_lis=zk.get("/zlist")
			check_list=check_lis[0]
			lis_mixed=check_list.split(" ")
			for i in range (0,len(lis_mixed),2) :
				port_list.append(int(lis_mixed[i]))

			for j in range (1,len(lis_mixed),2) :
				name_list.append(str(lis_mixed[j]))

			i= str(str(port_list[4])+" "+name_list[4])
			zk.create(name_list[4],i, ephemeral=True)
			serverSocket = socket(AF_INET,SOCK_STREAM) 
			serverSocket.bind(('',port_list[4])) 
			serverSocket.listen(1)
			
			if zk.exists("/bklist") :
				zk.set("/bklist","12000 /masternode 65000 /numnode 45678 /alphanode1 12000 /masternode1 12345 /alphanode")
				check_lis=zk.get("/bklist")
			check_list=check_lis[0]
			list_mixed=check_list.split(" ") 

			
			while 1 :
				if zk.exists("/zspec") and change==" " :
					t=zk.get("/zspec")
					bk_dict=ast.literal_eval(t[0])
					change="!!!"
					if len(bk_dict)>=len(alphadict):
						alphadict=bk_dict 
						print(alphadict)
				else :
					pass

				connectionSocket, addr = serverSocket.accept() 
				temp_variable = connectionSocket.recv(4096) 
				if temp_variable[0] in ['!','@','#','$','%','^','&','*','(',')','`'] :
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
							if zk.exists("/alphanode") :
								clientSocket = socket(AF_INET, SOCK_STREAM)
								t=zk.get("/alphanode")
								store=t[0].split(" ")
								back_num=int(store[0])
								clientSocket.connect(("0.0.0.0",back_num))
								clientSocket.send(temp_variable)
								clientSocket.close()
							else :
								pass
					else :
						pass

								

				elif temp_variable[0].isalpha() and temp_variable[0] in set2 :
					temp_var1=temp_variable.split(" ")
					if temp_var1[1]=="null" :
						key1=str(temp_var1[0])
						value=alphadict1[key1]
						print (value) 
						connectionSocket.send(value) 
						connectionSocket.close()	
					elif (temp_var1[0] not in alphadict1.keys()) or (temp_var1[0] in alphadict1.keys() and temp_var1[1]!=alphadict1[temp_var1[0]]):
						alphadict1[temp_var1[0]]=temp_var1[1] 
						if zk.exists("/zalpha1"):
							zk.set("/zalpha1",str(alphadict1))
						print(alphadict1)
						connectionSocket.send("the store has been updated")
						connectionSocket.close()
						if zk.exists("/alphanode1") :
							t=zk.get("/alphanode1")
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
						pass

				elif (temp_variable=="~!<>") :
					connectionSocket.send(str(lis_mixed))
					print("Just sent a list of port numbers and respective node names to the client!")
					connectionSocket.close()
			
				elif (temp_variable[0].isdigit()) or (temp_variable[0].isalpha() and temp_variable[0] not in set2) :
					connectionSocket.send(str(list_mixed))
					print("Just sent a list of back up port numbers and respective node names to the client!")
					print("Looks like a server is down or has changed it's name! Me to the rescue!")
					connectionSocket.close()

				else:
					pass
				

