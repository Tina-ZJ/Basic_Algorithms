# -*-coding:utf8 -*-
import sys



#定义节点
class Node(object):
	def __init__(self, key):
		self.key = key
		self.prev = None
		self.next = None

#定义双向链表
class DoubleList(object):
	def __init__(self):
		#链表头
		self.head = Node(None)
		#链表长
		self.length = 0
	
	#判断链表是否为空
	def isEmpty(self):
		if self.length==0:
			return True
		return False

	#遍历链表
	def traversal(self):
		if self.length == 0:
			return []
		#定义游标
		cur = self.head
		keys = list()
		for i in range(self.length):
			keys.append(cur.next.key)
			cur = cur.next
		return keys

	#插入链表头
	def insert_head(self, key):
		#构造新节点
		new_node = Node(key)
		#插入到表头 O(1)
		new_node.next = self.head.next
		new_node.prev = self.head
		self.head.next = new_node
		#链表长度加1
		self.length+=1

	#插入位置i
	def insert_pos(self, pos, key):
		#判断pos的有效性
		if isinstance(pos,int):
			if pos < 0 or pos>self.length :
				insert_head(key)
			else:
				new_code = Node(key)
				cur = self.head
				for i in range(self.length):
					if i==pos:
						# 设置新节点prev和next指向
						new_node.prev = cur
						new_node.next = cur.next
						# 更新指向新节点的节点
						cur.next = new_code
						new_code.next.prev = new_code
						# 链表长度更新
						self.length+=1
					else:
						cur = cur.next
		else:
			print("pos位置无效")

	#删除元素
	def delete(self, key):
		if self.isEmpty():
			print("list is empty")
		else:
			cur = self.head
			for i in range(self.length):
				if cur.next.key == key:
					if cur.next.next is None:
						#尾部节点删除
						cur.next = None
					else:
						#中间节点
						cur.next = cur.next.next
						cur.next.prev = cur
					#更新链表长度
					self.length-=1
				else:
					cur = cur.next
	#链表的搜索
	def search(self, key):
		cur = self.head
		for i in range(self.length):
			if cur.key != key:
				cur = cur.next
		return cur

if __name__ =="__main__":
	example = DoubleList()
	#插入元素
	for i in range(8):
		example.insert_head(i)
	#遍历
	print(example.traversal())
	#链表的长度
	print(example.length)
	#删除
	example.delete(3)
	print(example.traversal())
	print(example.length)
	#搜索
	x = example.search(4)
	print(x.key)
