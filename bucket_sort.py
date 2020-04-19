# -*-coding:utf8 -*-
import sys


def bucket_sort(A):
	n = len(A)
	# 初始化B
	B = [ [] for i in range(n) ]
	for i in range(n):
		#将A[i]插入B中
		B[int(n*A[i])].append(A[i])
	del A[:]
	for x in B:
		#对每个list x中的值进行排序，调用内部sorted排序函数,依次插入A中
		for i in sorted(x):
			A.append(i)
if __name__=='__main__':
	A = [.78,.17,.39,.26,.72,.94,.21,.12,.23,.68]
	print(A)
	bucket_sort(A)
	print(A)	
		
