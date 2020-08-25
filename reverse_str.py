# -*-coding:utf8 -*-
import sys


def reverseStr(str_list):
	lenth = len(str_list)
	mid = int(lenth/2)
	for i in range(mid):
		tmp = str_list[i]
		str_list[i] = str_list[lenth -i-1]
		str_list[lenth-i-1] = tmp
	
if __name__=='__main__':
	chars = ['H','a','n','h']
	print(chars)
	reverseStr(chars)
	print(chars)
