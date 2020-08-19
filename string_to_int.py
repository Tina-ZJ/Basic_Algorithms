# -*-coding:utf8 -*-

import sys



def StrToInt(s):
	#非法判断
	if s==None or len(s) < 1:
		raise Exception("string should not none")
	str2int = dict()
	data = list()
	result = 0
	for i in range(10):
		str2int[str(i)] = i
	for x in s:
		if x in str2int:
			data.append(str2int[x])
		elif x=='+' or x=='-':
			continue
		else:
			return 0
	for x in data:
		result=+result*10+x
	if s[0] == '-':
		result = 0 - result
	return result


if __name__=='__main__':
	s = '-1835+'
	print(StrToInt(s))
	print(type(StrToInt(s)))	
