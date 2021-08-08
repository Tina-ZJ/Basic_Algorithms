import numpy as np
import sys


def viterbi(score, trasition):
	"""
		输入
		score: [labelnum, seqlen], 发射分值
		trasition: [labelnum, labelnum], 转移概率, 这里假设每一层的label i 到label j 的转移的分值一致
		输出
		decode: [seqlen], path索引
	"""
	labelnum,seqlen = score.shape
	# 记录每一层到达该节点的最大累积分值
	trellis = score.copy()
	# 记录到达当前节点的最大分值路径的上一个节点索引位置 
	backpointers = np.zeros((labelnum,seqlen),dtype=int)
	# 全局分值最大路径path对应的节点索引
	decode = [0]*seqlen
	for i in range(1,seqlen):
		#转移分值加上发射分值
		tran_score = transition+trellis[:,i-1:i]
		#当前层的节点最大分值更新
		trellis[:,i] += np.max(tran_score, axis=0)
		#记录到达当前节点最大路径分值的上一层节点位置
		backpointers[:,i] = np.argmax(tran_score,axis=0)
	#记录最后一层分值最大的节点索引位置
	idxpath = np.argmax(tran_score[:,seqlen-1])
	#存储
	decode[seqlen-1] = idxpath
	print(trellis)
	print(backpointers)
	#读取最后一层最大值位置索引内容(上一层的节点位置），依次回溯）
	for t in range(seqlen-1,0,-1):
		idxpath = backpointers[idxpath,t]
		decode[t-1] = idxpath
	
	return decode
	

if __name__ == '__main__':
	score = np.array([[0.9, 0.1, 0.3],
         	[0.1, 0.8, 0.4],
         	[0.0, 0.1, 0.3]])
	transition = np.array([[0.1, 0.4, 0.5], [0.2, 0.7, 0.1], [0.9, 0.0, 0.1]])
	print(viterbi(score,transition))
