#Linked List implementation of a stack
#Author: Alex Toy
#Date: 9/28/21

class LLstack:
	
	def __init__(self):
		self.numNodes = 0
		self.tail = None
		
	def __iter__(self):
		self.n = self.numNodes
		self.index = self.tail
		return self
		
	def __next__(self):
		if (self.n == self.numNodes):
			self.n-=1
			return self.index.val
		if self.n>0:
			self.n-=1
			self.index = self.index.next
			return self.index.val
		else:
			raise StopIteration
		
	def push(self,val):
		self.numNodes+=1
		if (self.tail!=None):
			temp = self.Node(val)
			temp.next = self.tail
			self.tail = temp
		else:
			self.tail = self.Node(val)
			
	def pop(self):
		if (self.numNodes==0):
			return None
		self.numNodes-=1
		val = self.tail.val
		self.tail = self.tail.next
		return val
	
	def size(self):
		return self.numNodes
	
	
	class Node: 
		def __init__(self,val):
			self.val = val
			self.next = None
	

if __name__== "__main__":
	stack = LLstack()
	for i in range(100):
		stack.push(LLstack())
	i = iter(stack)
	for x in i:
		print(x)