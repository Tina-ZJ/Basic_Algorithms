# -*- coding -*-
import sys



def StepQuestion(n):
	# n=1 f(n)=1 n=2 f(n)=2
	L = [1,2]
	# n >2 f(n) = f(n-1) + f(n-2)
	for i in range(2,n):
		L.append(L[i-1]+L[i-2])

	return L[n-1]



if __name__=='__main__':
	n = 10
	print(StepQuestion(10))
	

