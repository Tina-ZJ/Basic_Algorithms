# -*-coding:utf8 -*-
import sys
import random

def permute_by_sorting(A):
	n = len(A)
	P = list()
	for i in range(n):
		#随机选择A[i]的排列权重
		randata = random.randint(1,n*n*n)
		P.append((A[i],randata))
	#根据每个A[i]的随机排列权重进行排序，到达随机数组A的目的
	result = sorted(P, key=lambda x:x[1])
	A_new = [ x[0] for x in result]
	return A_new


if __name__=='__main__':
	A = [1,2,3,4,5,6,7]
	A_sort = permute_by_sorting(A)
	print(A)
	print(A_sort)	
