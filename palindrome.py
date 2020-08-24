# -*-coding:utf8 -*-
import sys

#动态规划：分解子问题，把子问题的解存储起来，避免重复计算，这样就可以减低时间复杂度, 此次解的复杂度O(n*n)
def jugePalindrome(s):
	n = len(s)
	# d[i][j]代表子串[i,j]是否是一个回文串
	d = [[False]*n for _ in range(n)]
	# count for all palindrome string
	count = 0
	for i in range(n):
		for j in range(0, i+1):
			#子字符串长度
			length = i - j+1
			if length==1:
				d[j][i] = True
				count+=1
			elif length==2 and s[i]==s[j]:
				d[j][i] = True
				count+=1
			#前后相等且，中间也是回文字符串
			elif length>2 and s[i]==s[j] and d[j+1][i-1] is True:
				d[j][i] = True
				count+=1
	return count


if __name__=='__main__':
	s = 'aaa'
	print(jugePalindrome(s))
