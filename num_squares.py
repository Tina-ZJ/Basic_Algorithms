# -*-coding:utf8 -*-
import sys
import math

def num_squares(n):
	square_nums = [i*i for i in range(0, int(math.sqrt(n))+1)]
	dp = [float('inf')] * (n+1)
	dp[0] = 0
	for i in range(1, n+1):
		for square in square_nums:
			if i < square:
				break
			dp[i] = min(dp[i], dp[i-square] +1)
	return dp[-1]



if __name__=='__main__':
	test = [12,13,81,0]
	for n in test:
		print(num_squares(n))
