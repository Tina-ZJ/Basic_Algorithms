# -*-coding:utf8 -*-

def num_sqrt(n):
	'''
		二分查找，求一个整数的平方根
	'''
	# l, r分别代表上界和下界
	l,r = 0.0,float(n)
	# 初始化结果
	ans = -1
	while(l<=r):
		mid = (l+r)/2
		if mid * mid <= n:
			ans = mid
			l = mid + 1
		else:
			r = mid -1
	return ans



if __name__=='__main__':
	n = 82
	print(num_sqrt(n))				 
