# -*-coding:utf8 -*-
import sys


# 维持最大堆的性质
def max_heapify(A, i, size):
	# 节点i的左孩子, 由于python 索引是从0开始，不是从1开始，所以左 2*i --> 2*i+1   右 2*i+1 --> 2*i+2
	l = 2*i+1
	# 节点i的右孩子
	r = 2*i + 2
	#size = len(A)
	size = size
	if l<size and A[l]>A[i]:
		largest = l
	else:
		largest = i
	if r<size and A[r]>A[largest]:
		largest = r
	if largest!=i:
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		# 以largest为根节点的子树，可能又违背最大堆性质，所以需要继续递归调用
		max_heapify(A, largest, size)


#建堆，自顶向下方法，把一个大小为n的数组A，转换为最大堆
def build_max_heap(A):
	size = len(A)
	mid = int(size/2) - 1
	#从堆的性质得出 A[mid+1..size]都是树的叶节点，所以只需要对其他节点调用max_heapify，保证最大堆的性质就可
	for i in range(mid,-1,-1):
		max_heapify(A,i, size)
	return A

def heap_sort(A):
	#建堆
	build_max_heap(A)
	print(A)
	length = len(A)
	#最大元素总在根节点A[0]，通过与最后一个节点交换A[length-1]，新的节点需要维持最大堆性质，同时每次去掉交换后的最后一个节点
	for i in range(length-1,0,-1):
		# chage A[0] with A[i]
		temp = A[i]
		A[i] = A[0]
		A[0] = temp
		max_heapify(A,0, i)
	return A
if __name__=='__main__':
	A = [4,1,3,2,16,9,10,14,8,7]
	print(A)
	A = heap_sort(A)
	print(A)
		
