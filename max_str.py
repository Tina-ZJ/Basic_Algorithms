#-*-coding:utf8 -*-

import sys


def max_str(s):
	'''
		求一个字符串的无重复字符的最长子串
	'''
	maxs = 0
	data = dict()
	b = 0
	for i, x in enumerate(s):
		if x not in data:
			data.setdefault(x,-1)
			length = i - b +1
			if maxs < length:
				maxs = length
		else:
			# 一旦有重复的，需要重新移动
			b = i
	return maxs


if __name__=='__main__':
	test = ['abcabcbb','bbbbb','pwwkew']	
	for s in test:
		print(max_str(s))		
