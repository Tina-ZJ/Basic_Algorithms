#_*_coding:utf8 -*-
import sys

class Node:
	def __init__(self):
		self.child = dict()
		self.words = list()

class PrefixMath:
	def __init__(self, root):
		self.root = root
	def addWord(self, word):
		cur = self.root
		for ch in word:
			if ch not in cur.child:
				cur.child[ch] = Node()
			cur = cur.child[ch]
			cur.words.append(word)
			cur.words.sort()
			#if len(cur.words) > 3:
			#	cur.words.pop()
	def search(self, searchword):
		ans = list()
		cur = self.root
		flag = False
		for ch in searchword:
			if flag or ch not in cur.child:
				ans.append(list())
				flag = True
			else:
				cur = cur.child[ch]
			ans.append(cur.words)
		return ans


if __name__=='__main__':
	root = Node()
	example = PrefixMath(root)
	terms = ['我爱','中国人','国土', '国民','中国话', '中南',"中日"]
	for word in terms:
		example.addWord(word)
	result = example.search('中国')
	print(result)	
	
