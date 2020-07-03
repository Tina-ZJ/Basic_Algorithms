# -*-coding:utf8-*-
import sys

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = []
	# add edges
	def add_edge(self, s, d, w):
		self.graph.append([s, d, w])

	# print the solution
	def print_solution(self, dist):
		print(" Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))

	def bellman_ford(self, src):
		# step 1: fill the distance array and predecessor array
		dist = [float("Inf")] * self.V
		# Mark the source vertex
		dist[src] = 0
		
		# step 2 : relax edges |V|-1 times
		for _ in range(self.V - 1):
			for s, d, w in self.graph:
				if dist[s]!= float("Inf") and dist[s] + w < dist[d]:
					dist[d] = dist[s] + w
		# step 3: detect negative cycle
		for s, d, w in self.graph:
			if dist[s] != float("Inf") and dist[s] + w < dist[d]:
				print("Graph contains negative weight cycle")
				return 

		# No negative weight cycle found, print the distance
		self.print_solution(dist)
	

if __name__=='__main__':
	g = Graph(5)
	for s,d,w in [(0,1,4),(0,2,2),(1,2,3),(2,1,1),(1,3,2),(1,4,3),(2,4,5),(2,3,4),(4,3,-5)]:
		g.add_edge(s,d,w)
	g.bellman_ford(0)	
