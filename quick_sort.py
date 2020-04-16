# -*-coding:utf8 -*-
import sys
import random
#数组划分函数
def partition(A,p,r):
	#用最后一个值作为左右分割值
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j]<=x:
			i+=1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i+1]
	A[i+1] = A[r]
	A[r] = temp
	return i+1

#随机选择主元素，保证平衡划分
def randomized_partition(A,p,r):
	i = random.randint(p,r)
	# exchage A[r] with A[i]
	temp = A[r]
	A[r] = A[i]
	A[i] = temp
	return partition(A,p,r)

#快速排序算法
def quick_sort(A,p,r):
	if p<r:
		q = randomized_partition(A, p, r)
		quick_sort(A, p, q-1)
		quick_sort(A, q+1, r)


if __name__=='__main__':
	A = [2,8,7,1,3,5,6,4]
	print(A)
	quick_sort(A,0,len(A)-1)
	print(A)
