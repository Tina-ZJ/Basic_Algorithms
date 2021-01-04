# -*-coding:utf8 -*-
import sys
import numpy as np

def edit_distance(string1, string2):
	'''
		动态规划三部曲：
		1.初始化dp,定义好size
		2.dp的边界值计算好
		3.递增的顺序计算dp中每个元素的值
		4.返回dp最后一个元素值
	'''
		
	m = len(string1)
	n = len(string2)
	#距离矩阵初始化, d[i][j]代表string1[0:i-1]转变为string2[0:j-1]的最小步数
	d = np.zeros((m+1, n+1))
	#边界处理,string1到空string2的删除次数 
	for i in range(0,m+1):
		d[i,0] = i
	#空string1到string2的插入次数
	for j in range(0,n+1):
		d[0,j] = j
	#其它情况，插入，删除，替换取最小
	for i in range(1, m+1):
		for j in range(1, n+1):
			#sting1的第i个字符和string2的第j个字符相等，则替换操作为0
			if string1[i-1]==string2[j-1]:
				d[i,j] = min(d[i,j-1]+1, d[i-1,j]+1, d[i-1][j-1]+0)
			else: 
				d[i,j] = min(d[i,j-1]+1, d[i-1,j]+1, d[i-1][j-1]+1)
	return d[m,n]

if __name__=='__main__':
	string1 = 'abcdefg'
	string2 = 'cdeig'
	print(edit_distance(string1, string2))
		
