# -*-coding:utf8 -*-
import sys
maxs = sys.maxsize

def insert_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i -1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

    return A

if __name__=='__main__':
	A = [1,2,34,35,23,56,2,13]
	print(A)
	A = insert_sort(A)
	print(A)
