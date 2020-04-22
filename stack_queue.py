# -*-coding:utf8 -*-
import sys

#栈的基本操作
class Stack(object):
	#栈初始化为空
	def __init__(self):
		self.stack = []
	def isempty(self):
		return len(self.stack)==0
	#入栈
	def push(self, item):
		self.stack.append(item)
	#出栈
	def pop(self):
		return self.stack.pop()
	def size(self):
		return len(self.stack)

#队列的基本操作
class Queue(object):
	def __init__(self):
		self.queue = []
	def isempty(self):
		return len(self.queue)==0
	#入队列
	def enqueue(self,item):
		self.queue.insert(0,item)
	#出队列
	def dequeue(self):
		self.queue.pop()
	def size(self):
		return len(self.queue)


if __name__=='__main__':
	example = Stack()
	example2 = Queue()
	print(example.isempty())
	print(example2.isempty())
	example.push('a')
	example.push('d')
	example2.enqueue('a')
	example2.enqueue('d')
	print(example.isempty())
	print(example2.isempty())
	print(example.stack)
	print(example2.queue)
	example.pop()	
	example2.dequeue()	
	print(example.stack)
	print(example2.queue)
