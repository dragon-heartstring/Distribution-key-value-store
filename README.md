# Distribution-key-value-store
This program is used to store key-value pairs across a cluster of servers depending on type of key.
We decided to segregate our key value pairs on the basis of alphabets, digits and special characters.
Each of the primary servers (store for a particular type of key-value pair) is also a backup server (for another type of key-value pair)
The project comprises of a master server that is responsible for providing the clients with port numbers to establish a connection with the appropriate server.
The master is also responsible to provide the port number of the respective back up server when the primary server fails.
We have implemented high availability in the project through automatic updating of servers with key value pairs stored in their backup servers once the primary servers come back online.
We have also ensured if the master fails any of the remaining servers can take up the responsibilities of the master along with carrying out it's own duties/tasks.
We have zookeeper and socket programming to implement this program.

-> Switch on all servers beginning with the master server

-> Then switch on the client 

-> Input key-value pairs to store them in dictionaries across servers.

-> Input key  and leave value empty to get the value if it exists in the servers.

