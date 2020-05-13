# -*-coding:utf8 -*-
import sys

#构造节点
class Node(object):
	def __init__(self, key, code=0, parent=None,lchild=None, rchild=None):
		self.key = key
		self.code = code
		self.parent = parent
		self.lchild = lchild
		self.rchild = rchild


class HuffmanTree(object):
	def __init__(self,root=None):
		self.huffman_tree = []
		self.root = root
	#找两个key值最小的节点
	def find2node(self, flag):
		mini = []
		for i in range(len(self.huffman_tree)):
			if i in flag:
				continue
			if len(mini) < 2:
				mini.append(i)
			else:
				if self.huffman_tree[i].key < max([self.huffman_tree[mini[0]].key, self.huffman_tree[mini[1]].key]):
					pos = 0 if self.huffman_tree[mini[0]].key > self.huffman_tree[mini[1]].key else 1
					mini[pos] = i
		# let lchird.key < rchild.key
		if self.huffman_tree[mini[0]].key > self.huffman_tree[mini[1]].key:
			temp = mini[0]
			mini[0] = mini[1]
			mini[1] = temp
		#return sorted(mini)
		return mini
 

	def build(self, C):
		#flag记录已经合并的节点
		flag = []		
		#初始化各关键字key节点
		n = len(C)
		for key in C:
			self.huffman_tree.append(Node(key))
		#构建hufuman，n个值，需要n-1次合并操作
		for i in range(n,2*n-1):
			mini = self.find2node(flag)
			print(str(mini[0])+'\t'+str(mini[1]))		
			#合并的节点记录,下次合并不需要考虑		
			flag.append(mini[0])
			flag.append(mini[1])
			#构建新的Node节点，key为两个子节点key相加
			key = self.huffman_tree[mini[0]].key + self.huffman_tree[mini[1]].key
			node = Node(key,lchild=self.huffman_tree[mini[0]],rchild=self.huffman_tree[mini[1]])
			#新节点加入
			self.huffman_tree.append(node)
			self.huffman_tree[mini[0]].parent = node
			self.huffman_tree[mini[1]].parent = node
			self.huffman_tree[mini[1]].code = 1	

		#记录root节点
		print(node.key)
		self.root = node  
		
	#中序遍历
	def inorder_tree_walk(self, tree):
		if tree is not None:
			self.inorder_tree_walk(tree.lchild)
			print(tree.key, end=" ")
			self.inorder_tree_walk(tree.rchild)

	#获取节点的编码
	def huffman_code(self, cur):
		path = []
		while cur.parent!=None:
			#path结果保存从根节点搜索路径的编码结果
			path.insert(0,cur.code)
			cur = cur.parent
		return path	
				 
if __name__=='__main__':
	tree =  HuffmanTree()
	C = [5,9,12,13,16,45]
	tree.build(C)
	tree.inorder_tree_walk(tree.root)
	print()
	#打印每个叶子节点的赫夫曼编码
	for i in range(len(C)):
		path = tree.huffman_code(tree.huffman_tree[i])
		print('key='+str(tree.huffman_tree[i].key))
		print(path)	




