# -*-coding:utf8-*-

class Node:
	def __init__(self, value=0):
		self.value = value
		self.child = dict()
		self.is_word = False
		self.id = -1


class WordTrie:
	def __init__(self):
		self.root = Node()

	def insert(self, word, index):
		cur = self.root
		for ch in word:
			if ch not in cur.child:
				cur.child[ch] = Node(ch)
			cur = cur.child[ch]
		# 最后叶子节点结束标识为true，表明一个单词
		cur.is_word = True
		#该单词索引
		cur.id = index

	def search(self, content, wordList):
		size = len(content)
		res = [[] for i in range(len(wordList)) ]
		#遍历每个字符开头的前缀
		for i in range(len(content)):
			cur = self.root
			#从第i个开头的前缀直到字符结束进行匹配
			for j in range(i, len(content)):
				if content[j] in cur.child:
					cur = cur.child[content[j]]
					if cur.is_word:
						res[cur.id].append(i)
				else: break	
		return res


if __name__=='__main__':
		
	example = WordTrie()
	content = 'mississippi'
	wordList = ["is","ppi","hi","sis","i","ssippi"]
	for i, word in enumerate(wordList):
		example.insert(word, i)
	res = example.search(content, wordList)	
	print(res)	
