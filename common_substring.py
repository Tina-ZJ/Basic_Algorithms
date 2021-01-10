# -*- coding -*-
import sys
import numpy as np


def getCommon(s1, s2):
	'''
		求两个字符串的公共长，动态规划求解
	'''
	m = len(s1)
	n = len(s2)
	# save common len
	d = np.zeros((m+1,n+1), dtype=int)
	# max sub len
	maxlen = 0
	# the last substring index
	index = 0
	for i in range(m):
		for j in range(n):
			if s1[i]==s2[j]:
				d[i+1][j+1] = d[i][j] + 1
			if d[i+1][j+1] > maxlen:
				maxlen = d[i+1][j+1]
				index = i
	return maxlen, d[m,n],s1[index+1-maxlen:index+1]


if __name__=='__main__':
	s1 = 'acdeffghidk'
	s2 = 'acdkrfghidk'
	maxlen, maxlen2, substring = getCommon(s1, s2)
	# maxlen=maxlen2
	print(maxlen)	
	print(maxlen2)	
	print(substring)	
