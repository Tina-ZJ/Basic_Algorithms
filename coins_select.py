# -*-coding:utf8 -*-
import sys


def coins_way(n):
	coins = [1, 5, 10, 25]
	# dp[i][j]表示前i个coin组成j值的方式数量
	dp = [[0 for _ in range(n+1)] for _ in range(len(coins)+1)]
	# init 
	for i in range(len(coins)+1):
		dp[i][0] = 1
	for i in range(1, len(coins)+1):
		for j in range(1, n+1):
			if j < coins[i-1]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
	return dp[-1][-1]


if __name__=='__main__':
	print(coins_way(100)) 
