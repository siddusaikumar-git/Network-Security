
from mininet.topo import Topo
import random
from random import randint

class MyTopo( Topo ):

	def build( self ):

		f = open('data2.txt')
		lines = f.readlines()
		f.close()

		hosts = {}
		routers = {}
		routerLinks = {}
		count = 0
		nodeSet = set()
		for i in lines:

			node = int(i.split(":")[0])
			targets = [int(l) for l in list(i.split(":")[1].split(', ')) if l != '\n']
			print(node)
			hosts[node] = self.addHost(str(node))
			routers[node] = self.addSwitch('r' + str(node))
			nodeSet.add(node)
			for target in targets:
				if node not in routerLinks:
					routerLinks[node] = []
				routerLinks[node].append(target)
				if target not in nodeSet:
					hosts[target] = self.addHost(str(target))
					routers[target] = self.addSwitch('r' + str(target))\

				nodeSet.add(target)
	   		
		for key, values in routerLinks.items():
			for value in values:
				self.addLink(routers[key], routers[value])

		for key, value in hosts.items():
			self.addLink(value, routers[key])

topos = { 'mytopo': ( lambda: MyTopo() ) }