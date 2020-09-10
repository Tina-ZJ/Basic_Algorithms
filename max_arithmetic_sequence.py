# -*-coding:utf8 -*-
import sys


def max_sequence(L):
	'''
		求最大等差数列，中间可以不连续，只要构成等差数列
	'''
	length = len(L)
	if length <3:
		return length

	dp = [{} for i in range(length)]
	result = 0
	for i in range(1, length):
		for j in range(i):
			dis = L[i] -L[j]
			x = dp[j].get(dis, 1) +1
			dp[i][dis] = x
		result = max(result, max(dp[i].values()))
	return result


if __name__=='__main__':
	for x in [[3,6,9,12], [9,4,7,2,10], [20,1,15,3,10,5,8]]:
		print(max_sequence(x))
	
