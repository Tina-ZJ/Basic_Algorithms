# -*-coding:utf8 -*-
import sys


#要求：矩阵只能向右边或者下边移动
def sumPath(m,n):
	'''
	时间复杂度O(m*n),空间复杂度O(m*n)
	'''
	dp = [[0]*n for i in range(m)]
	#初始化边界
	for i in range(m):
		dp[i][0] = 1
	for j in range(n):
		dp[0][j] = 1
	#动态规划部分
	for i in range(1,m):
		for j in range(1,n):
			dp[i][j] = dp[i-1][j]+dp[i][j-1]
	return dp[-1][-1]

def sumPath_optimiz(m,n):
	'''
	时间复杂度O(m*n)，空间复杂度O(m)
	'''
	dp = [1]*m
	for j in range(1,n):
		for i in range(1,m):
			dp[i] = dp[i-1]+dp[i]
	return dp[-1]


if __name__=='__main__':
	m = 7
	n = 3
	print(sumPath(m,n))
	print(sumPath_optimiz(m,n))
