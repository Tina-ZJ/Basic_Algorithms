# -*-coding:utf8 -*-
import sys
from quick_sort_topk import quick_sort




def topk(a,k):
	'''
		若k个结果有序，冒泡排序，o(n*k)，若不要求有序，则堆排序o(nlg(k))
	'''
	lens = len(a)
	# 冒泡排序，o(n*k)
	for i in range(k):
		for j in range(lens-1):
			if (a[j]>a[j+1]):
				temp = a[j]
				a[j]=a[j+1]
				a[j+1]=temp
	print(a)
	return a[lens-k:]


if __name__=='__main__':
	a = [2,3,17,3,4,19,1,10,100,21,209,2,45,8,70,12,15,26,290]
	k = 5
	print(a)
	print(topk(a,k))
	quick_sort(a,0,len(a)-1, k)	
	print(a[:k])	
