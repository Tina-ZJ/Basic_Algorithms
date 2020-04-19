# -*-coding:utf8 -*-
import sys


def counting_sort(A, B, k):
	# let C[0..max_num] be a new array
	C = [0]*(k+1)
	#遍历A中的每个元素，如果一个输入的元素值为i，则将C[i]值加1
	for i in range(len(A)):
		C[A[i]]+=1
	#计算C中有多少个是小于等于i
	for i in range(1,k+1):
		C[i] = C[i]+C[i-1]
	#计数排序, B索引从0开始，所以每次A[i]放入的位置，由C[A[i]]-1
	#i从A的最后一个元素开始遍历，依次向前，保证计数排序的稳定性
	for i in range(len(A)-1,-1,-1):
		B[C[A[i]]-1] = A[i]
		C[A[i]]-=1
	return B

if __name__=='__main__':
	A = [2,5,0,2,3,0,3]
	print(A)
	k = max(A)
	B = [0]*len(A)
	B = counting_sort(A,B,k)
	print(B) 
