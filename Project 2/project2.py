
from mininet.topo import Topo
import random
from random import randint

class MyTopo( Topo ):

	def build( self ):

		# reading data file with nodeID range 350 to 400
		f = open('data.txt')
		lines = f.readlines()
		f.close()

		# Initializing clients, servers and routers dictionaries
		clients = {}
		servers = {}
		routers = {}
		ind =0
		nodeList = set()

		# Iterating through each line from the text file
		for i in lines:

			# capturing the routers and their respective connections in network
			node = int(i.split(":")[0])
			targets = [int(l) for l in list(i.split(":")[1].split(', ')) if l != '\n']
			
			# clients and servers are added as hosts to network
	   		clients[node] = self.addHost('c' + str(node)) 
	   		servers[node]  = self.addHost('s' + str(node))

	   		# adding routers as swithces to the network
	   		if node not in routers:
	   			routers[node]  = self.addSwitch('r' + str(node))
	   		nodeList.add(node)

	   		# Adding targets routers to network also connection between routers as links
	   		for target in targets:
	   			if target not in nodeList:
	   				routers[target]  = self.addSwitch('r' + str(target))
	   				nodeList.add(target)
	   				self.addLink(routers[node],routers[target])
	   		
	   		# Adding clients and servers to respective routers in network.
	   		self.addLink(clients[node] , routers[node])
	   
	   		self.addLink(servers[node], routers[node])


topos = { 'mytopo': ( lambda: MyTopo() ) }