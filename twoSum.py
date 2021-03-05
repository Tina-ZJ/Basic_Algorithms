# -*-coding:utf8 -*-

import sys

def twoSum(nums, target):
	data = dict()
	for i, num in enumerate(nums):
		data[num] = i

	for i in range(len(nums)):
		idx = data.get(target - nums[i], -1)
		if idx !=-1 and idx != i:
			print('(%s, %s)' % (str(i), str(idx)))


if __name__=='__main__':
	nums = [2,3,4,1,5]
	target = 5
	twoSum(nums, target)
