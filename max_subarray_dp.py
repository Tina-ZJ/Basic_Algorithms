# -*-coding:utf8 -*-
import sys

#动态规划求解，时间复杂度O(n)，空间复杂度O(1)
def maxSubArray(array):
	for i in range(1, len(array)):
		array[i] = max(array[i-1]+array[i], array[i])

	print(array)
	return max(array)



if __name__=='__main__':
	array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print(array)
	print(maxSubArray(array))	
