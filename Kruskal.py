# -*-coding:utf8 -*-
import sys


class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
	
	def add_edge(self, u, v, w):
		self.graph.append([u,v,w])

	# 找到节点所在的树的根节点
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# 合并新的节点到一棵树中来
	def apply_union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] +=1

	def kruskal(self):
		result = []
		i, e = 0, 0
		#排序，边按照权重从小到大排序
		self.graph = sorted(self.graph, key=lambda item: item[2])
		parent = []
		rank = []
		#初始，每个节点构成一棵树，根节点就是自己
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
		# 做V-1条节点选择
		while e < self.V - 1:
			u, v, w = self.graph[i]
			i = i+1
			x = self.find(parent, u)
			y = self.find(parent, v)
			# 选择的边的两个节点不在同一棵树,则合并
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.apply_union(parent, rank, x, y)
		#打印每一次选择的边
		for u, v , weight in result:
			print("%d - %d: %d" % (u, v, weight))


if __name__=='__main__':
	g = Graph(6)
	for x,y,w in [(0,1,4),(0,2,4),(1,2,2),(1,0,4),(2,0,4),(2,1,2),(2,3,3),(2,5,2),(2,4,4),(3,2,3),(3,4,3),(4,2,4),(4,3,3),(5,2,2),(5,4,3)]:
		g.add_edge(x,y,w)
	g.kruskal()
