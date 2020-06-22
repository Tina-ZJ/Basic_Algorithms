# -*-coding:utf8 -*-
import sys
import collections


'''
节点定义: 值，next指针
'''
class AdjNode:
	def __init__(self, key):
		self.vertex = key
		self.next = None

'''
图定义
'''
class Graph:
	def __init__(self, num):
		self.V = num
		self.graph = [None] * self.V
	
	# add edges
	def add_edge(self, s, d):
		node = AdjNode(d)
		#链表的插入
		node.next = self.graph[s]
		self.graph[s] = node
		#无向图,另一边链表也需更新
		node = AdjNode(s)
		node.next = self.graph[d]
		self.graph[d] = node

	#依次输出	
	def print_graph(self):
		for v in range(self.V):
			print("Vertex "	+str(v) + ":", end="")
			temp = self.graph[v]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print("\n")
	
	# BFS: Breadth first search
	def bfs(self, root):
		#记录访问的结点visited，先进先出队列
		visited, queue = list(), collections.deque([root])
		visited.append(root)
		while queue:
			# Dequeue a vertex from queue
			vertex = queue.popleft()
			#print(vertex)
			# 该节点的neighbours
			node = self.graph[vertex]
			while node:
				if node.vertex not in visited:
					visited.append(node.vertex)
					queue.append(node.vertex)
				node = node.next
		return visited
	# DFS: Depth first search
	def dfs(self, root, visited=None):
		if visited is None:
			visited = list()
		visited.append(root)
		#print(root)
		node = self.graph[root]
		while node:
			if node.vertex not in visited:
				self.dfs(node.vertex, visited)
			node = node.next
		return visited
 
if __name__ == "__main__":
	V = 6
	graph = Graph(V)
	for s, d in [(0,1),(0,2),(0,3),(1,2),(2,4),(4,5)]:
		graph.add_edge(s,d)
	# print
	print("链表存储输出") 
	graph.print_graph()
	print("BFS遍历")
	visited = graph.bfs(0)
	print(visited)
	print("DFS遍历")
	visite = graph.dfs(0) 
	print(visite)
