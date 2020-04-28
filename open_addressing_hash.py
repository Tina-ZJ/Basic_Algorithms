# -*-coding:utf8 -*-
import sys

class OpenAddrssHash(object):
	def __init__(self,size):
		#初始化散列表A，大小为size
		self.T = [None]*size
		self.size = size
	
	#双重散列表定义
	def double_hash(self, k,i):
		h1 = k % self.size
		h2 = 1 + k%(self.size-2)
		h = (h1 + i*h2) % self.size
		return h

	#向散列表T中插入k，并返回槽位j
	def hash_insert(self, k):
		i = 0
		while i<self.size:
			j = self.double_hash(k, i)
			if self.T[j] == None:
				self.T[j] = k
				return j
			i+=1
		return "hash table overflow"
	#向散列表T中搜索关键词k，返回槽位j
	def hash_search(self, k):
		i = 0
		j = self.double_hash(k,i)
		while self.T[j]!=None and i<self.size:
			j = self.double_hash(k,i)
			if self.T[j]==k:
				return j
			i+=1
		return None

if __name__=='__main__':
	example = OpenAddrssHash(13)
	#插入
	for k in [79,69,98,72,14,50]:
		print(example.hash_insert(k))
	#查找
	for k in [79,98,14,900]:
		print(example.hash_search(k))

	
