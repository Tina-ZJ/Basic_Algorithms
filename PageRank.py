# -*-coding:utf8 -*-
import sys
import numpy as np 


def pagerank(graph):
	'''
		简单实现pagerank迭代过程
	'''
	pr = np.array([1, 1, 1, 1]) #init node
	d = 0.85   
	for iter in range(10):
		pr = (1-d) + d * np.dot(graph, pr)
		print(iter)
		print(pr)


if __name__=='__main__':
	graph = np.array([[0,0,0,0],
					  [0,0,0,0],
					  [1, 0.5, 0, 0],
					  [0,0.5,0,0]])
	pagerank(graph)
