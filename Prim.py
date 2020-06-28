# -*-coding:utf8 -*-
import sys
INF = 9999999


class Graph: 
	def __init__(self, V, G):
		self.V = V
		self.G = G

	def prim(self):
		selected = [0] * self.V
		no_edge = 0
		selected[0] = True
		print("Edge : Weight")
		#需要选择V-1个
		while (no_edge < self.V - 1):
			minimum = INF
			x = 0
			y = 0
			# 遍历V个节点 
			for i in range(V):
				#该节点选择了的
				if selected[i]:
					for j in range(self.V):
						#选择的邻接节点没有选择的，且有边的
						if ((not selected[j]) and self.G[i][j]):  
							if minimum > self.G[i][j]:
								minimum = self.G[i][j]
								x = i
								y = j
			print(str(x) + "-" + str(y) + ":" + str(self.G[x][y]))
			selected[y] = True
			no_edge += 1

if __name__=='__main__':
	V = 5
	G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]	
	graph = Graph(V,G)
	graph.prim()	
