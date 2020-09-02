#-*-coding:utf8 -*-
import sys

#双指针
def continuous_char(s):
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
	
