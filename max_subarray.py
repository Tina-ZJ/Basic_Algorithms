# -*-coding:utf8 -*-
import sys
mins = -sys.maxsize


#最大子数组横跨中间位置
def find_max_cross_subarray(A, low, mid, high):
	left_sum = mins
	sums = 0
	for i in range(mid, low-1, -1):
		sums+=A[i]
		if sums > left_sum:
			left_sum = sums
			max_left = i
	right_sum = mins
	sums = 0
	for i in range(mid+1, high+1):
		sums+=A[i]
		if sums > right_sum:
			right_sum = sums
			max_right = i
	return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(A, low, high):
	if low == high:
		return (low, high, A[low])
	else:
		mid = (low+high) / 2
		mid = int(mid)
		#mid的左边和右边分别递归调用自己
		(left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
		(right_low, right_high, right_sum) = find_max_subarray(A, mid+1, high)
		#第三种情况，子数组的开始和结束索引位于mid的左和右情况
		(cross_low, cross_high, cross_sum) = find_max_cross_subarray(A, low,mid, high)
		#三种情况，对比选择最大的返回，子数组的开始和结束索引，以及子数组求和值
		if left_sum >= right_sum and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)


if __name__ == "__main__":
	A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	low, high, sums = find_max_subarray(A,0,len(A)-1)
	print(str(low)+'\t'+str(high)+'\t'+str(sums))
	print(A[low:high+1]) 
