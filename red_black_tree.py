# -*-coding: utf8 -*-
import sys


#构造节点
class Node(object):
	def __init__(self, key, color='', parent=None,lchild=None, rchild=None):
		self.key = key
		self.parent = parent
		self.lchild = lchild
		self.rchild = rchild
		self.color = color

#二叉搜索树
class RBTree(object):
	def __init__(self,root=None):
		self.nil = Node(key=-1, color='BLACK')
		self.root = self.nil


	#左旋转
	def left_rotate(self, x):
		# set y
		y = x.rchild
		# turn y left subtree into x right subtree
		x.rchild = y.lchild
		if y.lchild != self.nil:
			y.lchild.parent = x
		# link x parent to y
		y.parent = x.parent
		if x.parent == self.nil:
			# x is root
			self.root = y
		elif x == x.parent.lchild:
			x.parent.lchild = y
		else:
			x.parent.rchild = y
		# put x on y left
		y.lchild = x
		x.parent = y

	#右旋转
	def right_rotate(self, y):
		# set x
		x = y.lchild
		# turn x right subtree into y left subtree
		y.lchild = x.rchild
		if x.rchild != self.nil:
			x.rchild.parent = y
		# link y parent to x
		x.parent = y.parent
		if y.parent == self.nil:
			# x is root
			self.root = x
		elif y == y.parent.lchild:
			y.parent.lchild = x
		else:
			y.parent.rchild = x
		# put y on x right
		x.rchild = y
		y.parent = x
		
	# insert
	def rb_insert(self, cur):
		#用
		y = self.nil
		x = self.root
		while x!=self.nil:
			#y记录插入的节点cur对应的parent节点
			y = x
			#对比关键字值，判断cur是插入左边还是右边
			if cur.key < x.key:
				x = x.lchild
			else:
				x = x.rchild
		cur.parent = y
		if y==self.nil:
			#第一次插入节点，树为空
			self.root = cur
		#判断插入左子树还是右子树
		elif cur.key < y.key:
			y.lchild = cur
		else:
			y.rchild = cur
		cur.lchild = self.nil
		cur.rchild = self.nil
		cur.color = 'RED'
		
		#保持红黑性质  to do: fix bug
		#self.rb_insert_fixup(cur)

	#红黑性质保持
	def rb_insert_fixup(self, cur):
		print(cur.key)
		while cur.parent.color == 'RED':
			if cur.parent == cur.parent.parent.lchild:
				y = cur.parent.parent.rchild
				if y.color == 'RED':
					cur.parent.color = 'BLACK'
					y.color = 'BLACK'
					cur.parent.parent.color = 'RED'
					cur = cur.parent.parent
				elif cur == cur.parent.rchild:
					cur = cur.parent
					self.left_rotate(cur)
				cur.parent.color = 'BLACK'
				cur.parent.parent.color = 'RED'
				self.right_rotate(cur.parent.parent)
			elif cur.parent == cur.parent.parent.rchild:
				y = cur.parent.parent.lchild

				if y.color == 'RED':
					cur.parent.color = 'BLACK'
					y.color = 'BLACK'
					cur.parent.parent.color = 'RED'
					cur = cur.parent.parent
				elif cur == cur.parent.lchild:
					cur = cur.parent
					self.left_rotate(cur)
				cur.parent.color = 'BLACK'
				cur.parent.parent.color = 'RED'
				self.right_rotate(cur.parent.parent)
			self.root.color = 'BLACK'

	#中序遍历
	def inorder_tree_walk(self, tree):
		if tree !=self.nil:
			self.inorder_tree_walk(tree.lchild)
			print(tree.key, end=" ")
			self.inorder_tree_walk(tree.rchild)


if __name__=='__main__':
	tree = RBTree()
	for x in [15,6,18,3,7,17,20,2,4,13,9]:
		x = Node(x)
		tree.rb_insert(x)

	#中序遍历结果
	tree.inorder_tree_walk(tree.root)
