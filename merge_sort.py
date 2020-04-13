# -*-coding:utf8 -*-
import sys
maxs = sys.maxsize

#归并两个已经排序好的数组
def merge(L,R):
	B = []
    #增加两个哨兵
	L.append(maxs)
	R.append(maxs)
	m,n = 0,0
    #总共循环两个数组长度-2次
	for i in range(len(L)+len(R)-2):
		if L[m]<=R[n]:
			B.append(L[m])
			m+=1
		else:
			B.append(R[n])
			n+=1
	return B

def merge_sort(A):
	if len(A)<=1:
		return A
	middle = int(len(A)/2)
	left = merge_sort(A[:middle])
	right = merge_sort(A[middle:])
	return merge(left,right)

if __name__=='__main__':
	A = [1,2,34,35,23,56,2,13]
	print(A)
	A = merge_sort(A)
	print(A)
