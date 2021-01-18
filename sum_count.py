 # -*-coding:utf8 -*-

# 1.边界条件   2.递推关系
def num_count(A, num):
	''' 给定一个数组A:例如[5,5,10,2,3]，求该数组和为num的组合数
		（索引序列不一致，就是一种不同的组合，若num=15, 有4种：
			[A[0],A[2]], [A[1],A[2]], [A[2],A[3],A[4]], [A[0],A[1],A[3],A[4]]
	'''
	dp = [[0]*(num+1) for _ in range(len(A)+1)]
	# init
	for i in range(len(A)+1): 
		dp[i][0] = 1
	for i in range(1, len(A)+1):
		for j in range(1, num+1):
			if j>=A[i-1]:
				dp[i][j] = dp[i-1][j]+dp[i-1][j-A[i-1]]
			else:
				dp[i][j] = dp[i-1][j]
	return dp[-1][-1]


if __name__=='__main__':
	A = [5, 5, 10, 2, 3]
	print(num_count(A, 15))
