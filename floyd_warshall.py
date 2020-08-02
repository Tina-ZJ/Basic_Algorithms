# -*-coding:utf8 -*-

import sys


INF= float("inf")

class Graph:
	def __init__(self, vertices, graph):
		self.vertices = vertices
		self.graph = graph
		self.distance = list(map(lambda i: list(map(lambda j:j,i)), self.graph))

	def floyd_warshall(self):
		for k in range(self.vertices):
			for i in range(self.vertices):
				for j in range(self.vertices):
					self.distance[i][j] = min(self.distance[i][j], self.distance[i][k]+self.distance[k][j])
	
	def show_result(self):
		for i in range(self.vertices):
			for j in range(self.vertices):
				if (self.distance[i][j] == INF):
					print("INF", end=" ")
				else:
					print(self.distance[i][j], end="  ")
			print(" ")


if __name__=='__main__':
	G = [[0, 3, INF, 5],
		 [2, 0, INF, 4],
		 [INF, 1, 0, INF],
		 [INF, INF, 2, 0]]
	verticies = 4
	example = Graph(verticies, G)
	example.floyd_warshall()
	example.show_result()
