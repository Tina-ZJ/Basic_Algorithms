# -*- coding:utf8 -*-
import sys


#构造节点
class Node(object):
	def __init__(self, key, parent=None,lchild=None, rchild=None):
		self.key = key
		self.parent = parent
		self.lchild = lchild
		self.rchild = rchild

#二叉搜索树
class BinaryTree(object):
	def __init__(self,root=None):
		self.root = root

	#构建二叉搜索树，插入节点
	def insert(self, cur):
		y = None
		x = self.root
		while x!=None:
			#y记录插入的节点cur对应的parent节点
			y = x
			#对比关键字值，判断cur是插入左边还是右边
			if cur.key < x.key:
				x = x.lchild
			else:
				x = x.rchild
		cur.parent = y
		if y==None:
			#第一次插入节点，树为空
			self.root = cur
		#判断插入左子树还是右子树
		elif cur.key < y.key:
			y.lchild = cur
		else:
			y.rchild = cur

	#先序遍历
	def preorder_tree_walk(self, tree):
		if tree is not None:
			print(tree.key, end=" ")
			self.preorder_tree_walk(tree.lchild)
			self.preorder_tree_walk(tree.rchild)

	#中序遍历
	def inorder_tree_walk(self, tree):
		if tree is not None:
			self.inorder_tree_walk(tree.lchild)
			print(tree.key, end=" ")
			self.inorder_tree_walk(tree.rchild)

	#后序遍历
	def postorder_tree_walk(self, tree):
		if tree is not None:
			self.postorder_tree_walk(tree.lchild)
			self.postorder_tree_walk(tree.rchild)
			print(tree.key, end=" ")

	#查找关键字为key的节点
	def search(self, cur, key):
		while cur !=None and key!=cur.key:
			if key < cur.key:
				cur = cur.lchild
			else:
				cur = cur.rchild
		return cur

	#查找最小关键字元素
	def minimum(self, cur):
		while cur.lchild!=None:
			cur = cur.lchild
		return cur

	#查找最大关键字元素
	def maximum(self, cur):
		while cur.rchild!=None:
			cur = cur.rchild
		return cur

	#查找节点cur的后继
	def successor(self, cur):
	#如果节点的右孩子不为空，那么x的后继恰是x右子树的最左节点，调用minimum(cur.rchild)可以找到
		if cur.rchild!=None:
			return self.minimum(cur.rchild)
		y = cur.parent
		#后继节点为最低的祖先，并且该节点的后继节点的左孩子也是该节点的祖先
		while y!=None and cur == y.rchild:
			cur = y
			y = y.parent
		return y
	#移动子树过程
	def transplant(self,u,v):
		#当u为树根的情况
		if u.parent == None:
			self.root = v
		#更新u.parent.lchid
		elif u == u.parent.lchild:
			u.parent.lchild = v
		#更新u.parent.rchild
		else:
			u.parent.rchild = v
		#允许v为None，若不为None，更新v.parent
		if v!=None:
			v.parent = u.parent

	#delete节点
	def delete(self, cur):
		#cur 节点没有左孩子
		if cur.lchild == None:
			self.transplant(cur, cur.rchild)
		# cur 有一个左孩子但没有右孩子
		elif cur.rchild == None:
			self.transplant(cur, cur.lchild)
		#cur有两个孩子
		else:
			#获取cur的后继节点
			y = self.minimum(cur.rchild)
			#如果y不是cur的左孩子，用y的右孩子替换y并成为y的双亲的一个孩子，
			#然后将z的右孩子转变为y的右孩子
			if y.parent != cur:
				self.transplant(y,y.rchild)
				y.rchild = cur.rchild
				y.rchild.parent = y
			#用y替换z，并成为z的双亲的一个孩子，再用z的左孩子替换y的左孩子
			self.transplant(cur,y)
			y.lchild = cur.lchild
			y.lchild.parent = y
				
if __name__=='__main__':
	tree = BinaryTree()
	#新元素插入树中
	for x in [15,6,18,3,7,17,20,2,4,13,9]:
		x = Node(x)
		tree.insert(x)
	#先序遍历结果
	tree.preorder_tree_walk(tree.root)
	print('\n')
	#中序遍历结果
	tree.inorder_tree_walk(tree.root)
	print('\n')
	#后序遍历结果
	tree.postorder_tree_walk(tree.root)
	print('\n')
	#查找
	x = tree.search(tree.root, 15)
	if x!=None:
		print(x.key)
		print("find key in the tree")
	else:
		print("not find key in the tree")
	#查找x后继节点
	y = tree.successor(x)
	print("x的后继节点关键值为: %s" % str(y.key))
	# 最小值
	z = tree.minimum(tree.root)
	print("最小值 %s" % str(z.key))
	#删除节点z,x
	tree.delete(z)
	tree.delete(x)
	#删除节点后的中序遍历结果
	tree.inorder_tree_walk(tree.root)
