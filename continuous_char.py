#-*-coding:utf8 -*-
import sys

#双指针
def continuous_char(s):
	'''
		求字符串最大相同子字符串长度
		双指针移动方式求解
	'''
	res = 1
	left, right = 0, 1
	while right < len(s):
		if s[right] != s[left]:
			res = max(right - left, res)
			left = right
		right += 1
	return max(right - left, res)



if __name__=='__main__':
	s = "hooraaaaaaaaaaaya"
	print(continuous_char(s))
	
