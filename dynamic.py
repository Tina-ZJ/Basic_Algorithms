# -*-coding:utf8 -*-
import sys

#### 自顶向下 ########
def cut_rod(p,n):
	if n == 0:
		return 0
	#初始化效益最小值
	q = -sys.maxsize
	for i in range(1,n+1):
		q = max(q,p[i]+cut_rod(p,n-i))
	return q

### 带备忘的自顶向下  #######
def memoized_cut_rod(p,n):
	#init the r[0..n]
	r = [-sys.maxsize for i in range(n+1)]
	return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p,n,r):
	#已经计算的子问题就直接返回
	if r[n]>=0:
		return r[n]
	if n == 0:
		q = 0
	else:
		q = -sys.maxsize
		for i in range(1,n+1):
			q = max(q, p[i]+memoized_cut_rod_aux(p, n-i, r))
	#记录每次已经计算的子问题解
	r[n] = q
	return q


#####  自底向上########
def bottom_up_cut_rod(p,n):
	#长度为0的钢条没有收益
	r = list()
	# let r[0] = 0
	r.append(0)
	for j in range(1,n+1):
		q = -sys.maxsize
		#求解规模为j的子问题解
		for i in range(1, j+1):
			q = max(q, p[i]+r[j-i])
		#将规模为j的子问题的解存入r[j]
		r.append(q)
	#返回最优解
	return r[n]


if __name__=='__main__':
	#给定切割价格p以及长度n,求切割最大收益,p[i]代表切割长度为i的钢条收益p[i]
	p = [0,1,5,8,9]
	n = len(p)-1
	print(cut_rod(p,n))
	print(memoized_cut_rod(p,n))
	print(bottom_up_cut_rod(p,n))
