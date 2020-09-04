# -*-coding:utf8 -*-
import sys

#时间复杂度O(m*n)，空间复杂度O(1),用原始矩阵存储，不需要额外空间
def minPath(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			#第一个初始值,不需要更新
			if i == j == 0:
				continue
			# i=0或者j=0边界处理
			elif i == 0: matrix[i][j] = matrix[i][j-1] + matrix[i][j]
			elif j == 0: matrix[i][j] = matrix[i-1][j] + matrix[i][j]
			# 当前位置值为从左边或者上面过来的两条路径最小分值
			else: matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + matrix[i][j]
	#返回矩阵最后一个元素路径最小分值
	return matrix[-1][-1]



if __name__=='__main__':
	matrix = [[1,3,1],[1,5,1],[4,2,1]]
	print(minPath(matrix))
