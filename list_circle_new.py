# -*-coding:utf8 -*-
import sys



class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


def JugeCircle(head):
	# 定义两个快慢指针，快指针一次走两步，慢指针一次走1步，如果有环，则快慢指针一定会重合, 时间复杂度O(n)，空间复杂度O(1)
	fast = head
	slow = head
	# 空和一个节点直接返回
	while fast and fast.next != None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return True
	return False


if __name__=='__main__':
	link_list = list()
	for x in range(4):
		link_list.append(Node(x))
	for i in range(len(link_list)-1):
		link_list[i].next = link_list[i+1]
	link_list[i+1].next = link_list[1]
	print(JugeCircle(link_list[0]))	
		
