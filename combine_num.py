# -*-coding:utf8 -*-
def combine_num(candidates, num):
	'''
	给定一个无重复的元素的数组candidates和一个目标数num， 找出candidates中所有可以使数字和为num的组合
	candidates中的数字可以无限制重复被选取
	'''
	candidates = sorted(candidates)
	result = []
	def find(s, use, remain):
		for i in range(s, len(candidates)):
			c = candidates[i]
			if c == remain:
				result.append(use + [c])
			elif c < remain:
				find(i, use + [c], remain -c)
			if c > remain:
				return
	find(0, [], num)
	
	return result


if __name__=='__main__':
	for c, n in zip([[2,3,6,7],[2,3,5]], [7,8]):
		print(combine_num(c,n))
