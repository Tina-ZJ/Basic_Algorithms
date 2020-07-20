# -*-coding:utf8 -*-
import sys

class Graph:
	def __init__(self, vertices, edgs):
		self.vertices= vertices
		self.edgs = edgs
		self.num_of_vertices = len(vertices[0])
		self.visited_and_distance = [[0,0]]

	def to_be_visited(self):
		v = -1
		for index in range(self.num_of_vertices):
			if self.visited_and_distance[index][0] == 0 and (v < 0 or self.visited_and_distance[index][1] <= self.visited_and_distance[v][1]):
				v = index
		return v

	def distance(self):
		for i in range(self.num_of_vertices-1):
			self.visited_and_distance.append([0, sys.maxsize])
		for vertex in range(self.num_of_vertices):
			# find next vertex to be visited
			to_visit = self.to_be_visited()
			for neighbor_index in range(self.num_of_vertices):
				if self.vertices[to_visit][neighbor_index] ==1 and self.visited_and_distance[neighbor_index][0] == 0:
					new_distance = self.visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
					if self.visited_and_distance[neighbor_index][1] > new_distance:
						self.visited_and_distance[neighbor_index][1] = new_distance
				self.visited_and_distance[to_visit][0] = 1

if __name__=='__main__':
	vertices = [[0, 0, 1, 1, 0, 0, 0],
				[0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

	edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

	graph = Graph(vertices, edges)
	graph.distance()
	i = 0
	for distance in graph.visited_and_distance:
		print("Distance of ", chr(ord('a')+i), "from source vertex: ", distance[1])
		i+=1	
