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

def randomized_select(A,p,r,i):
	if p == r:
		return A[p]
	q = randomized_partition(A, p, r)
	k = q-p+1
	if i == k:
		return A[q]
	elif i<k:
		return randomized_select(A, p, q-1, i)
	else:
        #在A[q+1,r]中的第i-k小的元素
		return randomized_select(A, q+1, r, i-k)


if __name__=='__main__':
	A = [2,8,7,12,10,51,16,4]
	print(A)
	x = randomized_select(A,0,len(A)-1, 3)
	print(x)
