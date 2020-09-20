# -*-coding:utf8 -*-
import sys

def gd(rate, epoch=10):
	'''
		y=x*x函数，梯度求解过程验证
	'''
	x = 10
	results = [x]
	for i in range(epoch):
		x -= rate*2*x
		results.append(x)
	print('epoch %d, x: %f'%(epoch,x))
	return results


if __name__=='__main__':
	gd(0.2, 10)
