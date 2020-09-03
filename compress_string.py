#-*-coding:utf8 -*-
import sys

#双指针
def continuous_char(s):
	result = list()
	left, right = 0, 1
	while right < len(s):
		if s[right] != s[left]:
			result.append(s[left])	
			result.append(str(right-left))	
			left = right
		right += 1

	#最后的边界需要加上来
	result.append(s[left])
	result.append(str(right-left))
	result = ''.join(result)
	if len(result)>len(s):
		return s
	return result



if __name__=='__main__':
	s = "aabccccca"
	print(continuous_char(s))
	
