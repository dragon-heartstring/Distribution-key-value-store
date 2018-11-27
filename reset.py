from kazoo.client import KazooClient,KazooState
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
if zk.exists("/zlist") :
	zk.set("/zlist","12000 /masternode 12345 /alphanode 65000 /numnode 45678 /alphanode1 45876 /specnode")

if zk.exists("/bklist") :
	zk.set("/bklist","12000 /masternode 65000 /numnode 45678 /alphanode1 45876 /specnode 12345 /alphanode")

if zk.exists("/zalpha") :
	zk.set("/zalpha","{}")

if zk.exists("/znum") :
	zk.set("/znum","{}")

if zk.exists("/zspec") :
	zk.set("/zspec","{}")

if zk.exists("/zalpha1") :
	zk.set("/zalpha1","{}")

zk.stop()
