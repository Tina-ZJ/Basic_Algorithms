# -*-coding:utf8 -*-

def isMatch(s, p):
	"""
	给定一个字符串（s)和一个字符模式(p)，实现一个支持'?'和'*'的通配符匹配
	eg:
	s = "aa"  p = "a"  false
	s = "cb"  p = "?b"  true
	s = "adceb" p="*a*b" true
	"""
	m, n = len(s), len(p)
	dp = [[False] * (n+1) for _ in range(m+1)]
	#边界处理
	dp[0][0] = True
	for i in range(1, n+1):
		if p[i-1] == '*':
			dp[0][i] = True
		else:
			break
	for i in range(1, m+1):
		for j in range(1, n+1):
			if p[j-1] == '*':
				dp[i][j] = dp[i][j-1] | dp[i-1][j]
			elif p[j-1] == '?' or s[i-1] == p[j-1]:
				dp[i][j] = dp[i-1][j-1]
	return dp[m][n]

if __name__=='__main__':
	s = "adceb"
	p = "*a*b"
	print(isMatch(s,p))	
