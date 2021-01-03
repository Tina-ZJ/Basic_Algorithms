# -*-coding:utf8 -*-
import sys


class Node:
	def __init__(self, elem):
		self.elem = elem
		self.next = None


def circle(Link):
	'''
	两个指针同时指向链表，慢指针每次走一步，快指针每次走2步，若有环
	则，慢指针会与快指针重合
	'''
	p1 = p2 = Llist
	while p2 and p2.next: #当块指针指向的链表后面的元素空或者只有一个元素了则跳出循环
		p1 = p1.next
		p2 = p2.next.next
		if p1 == p2:
			return True
	return False


if __name__=='__main__':
	Llist = Node(1)
	p1 = Node(2)
	p2 = Node(3)
	p3 = Node(4)
	Llist.next = p1
	p1.next = p2
	p2.next = p3
	p3.next = p2
	print(circle(Llist))
