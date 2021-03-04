# -*-coding:utf8 -*-

import sys

def wordSeg(s, wordDict):
	'''
		单词拆分，给定一个非空字符串s和一个包含非空单词的列表wordDict
		判断s是否可以被空格拆分为一个或多个在字典中出现的单词
	'''
	n = len(s)
	dp = [False] * (n+1)
	dp[0] = True
	for i in range(n):
		for j in range(i+1, n+1):
			if dp[i] and s[i:j] in wordDict:
				dp[j] = True
	print(dp)
	return dp[-1]


if __name__=='__main__':
	s = "catsanddog"
	wordDict = ["cats", "sand", "dog", "cat", "and"]
	print(wordSeg(s, wordDict))	
