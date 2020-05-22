# -*- coding:utf8 -*-
import sys


#构造节点
class Node(object):
	def __init__(self, n=0,isleaf = True):
		#节点关键字数量n
		self.n = n
		#关键字keys值
		self.keys = []
		# 孩子节点
		self.childs = []
		#是否是叶子节点
		self.leaf = isleaf
	@classmethod
	def allocate_node(self, key_max):
		node = Node()
		child_max = key_max+1
		#初始化key and child
		for i in range(key_max):
			node.keys.append(None)
		for i in range(child_max):
			node.childs.append(None)
		return node	


class BTree(object):
	def __init__(self, t, root=None):
		# B数的最小度数
		self.t = t
		#节点包含的关键字的最大个数
		self.max_key = 2*self.t-1
		#节点包含的最大孩子个数
		self.max_child = self.max_key+1
		#跟节点
		self.root = root

	'''
	   输入一个非满的内部节点x，和一个使x.child[i]为x的满子节点的下标i
	   把子节点分裂成两个，并调整x
	'''
	def btree_split_child(self, x, i):
		#分配一个新节点
		#z = Node()
		z = self.__new_node()
		#获取x的第i个孩子节点
		y = x.childs[i]
		#更新新生成的节点z
		z.leaf = y.leaf
		#分裂, y关键字2t-1变成t-1，z获取y中最右边的t-1个关键字
		z.n = self.t-1	
		#把y的t-1个关键字以及相应的t个孩子赋值z
		for j in range(self.t-1):
			z.keys[j] = y.keys[j+self.t]		
		if not y.leaf:
			for j in range(self.t):
				z.childs[j] = y.childs[j+self.t]
		#调整y的关键字个数
		y.n = self.t - 1
		# z插入为x的一个孩子
		for j in range(x.n+1, i, -1):
			x.childs[j] = x.childs[j-1]
		x.childs[i+1] = z
		#提升y的中间关键字到x来分割y和z
		for j in range(x.n, i-1, -1):
			x.keys[j+1] = x.keys[j]
		x.keys[i] = y.keys[self.t-1]
		#调整x的关键字个数
		x.n = x.n+1	
		
	'''
	将关键字k插入到节点x中，假定在调用过程中x是非满的
	'''
	def btree_insert_nonfull(self, x, k):
		i = x.n
		#x是叶子节点，直接插入
		if x.leaf:
			while i>0 and k<x.keys[i-1]:
				x.keys[i] = x.keys[i-1]
				i-=1
			x.keys[i] = k
			#更新节点数
			x.n+=1
		#非叶节点
		else:
			while i>0 and k<x.keys[i-1]:
				i-=1
			i+=1
			#判断是否递归降至一个满子节点
			if x.childs[i-1].n == 2*self.t-1:
				self.btree_split_child(x,i-1)
				#确定向两个孩子中哪个下降是正确的
				if k>x.keys[i-1]:
					i+=1
			#递归地将k插入合适的子树中	
			self.btree_insert_nonfull(x.childs[i-1],k)
	def __new_node(self):
		'''
		创建新的B树节点
		'''
		return Node().allocate_node(self.max_key)	
	'''
	插入，利用btree_insert_child保证递归始终不会降至一个满节点
	'''
	def btree_insert(self, k):
		# 检查是否为空树
		if self.root is None:
			node = self.__new_node()
			self.root = node	
		r = self.root
		#根节点是满节点
		if r.n == 2*self.t - 1:
			#s = Node()
			s = self.__new_node()
			# s成为新的根节点
			self.root = s
			s.leaf = False
			s.n = 0
			s.childs[0] = r
			#分裂根节点，对根进行分裂是增加b树高度的唯一途径
			self.btree_split_child(s,0)
			self.btree_insert_nonfull(s,k)
		else:
			self.btree_insert_nonfull(r,k)

	#遍历
	def btree_walk(self, btree):
		if btree is not None:
			

if __name__=='__main__':
	tree = BTree(3)
	for x in ['G','M','P','X','A','C','D','E','J','K','N','O','R','S','T','U','V','Y','Z']:
		tree.btree_insert(x)	
