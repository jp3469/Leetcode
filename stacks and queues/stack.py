class Stack(list):
	def peek(self):
		return self[-1]
	def push(self, item):
		self.append(item)
	def isEmpty(self):
		return len(self) == 0