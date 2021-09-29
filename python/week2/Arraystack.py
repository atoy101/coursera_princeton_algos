#array implementation of stack
#author:  Alex Toy
#date: 9/28/21

class arrayStack:
	
	def __init__(self):
		self.stack = [None]*1
		self.index = 0
		
	def __iter__(self):
		self.i = self.index
		return self
	def __next__(self):
		if self.i>0:
			self.i -=1
			return self.stack[self.i]
		else:
			raise StopIteration
		
	def push(self,val):
		if (self.index > 0 and self.index == len(self.stack)):
			self.resize(len(self.stack)*2)
		self.stack[self.index]= val
		self.index+=1
	
	def pop(self):
		if (self.index == len(self.stack)/4):
			self.resize(int(len(self.stack)/2))
		if (self.index > 0):
			self.index-=1
			val = self.stack[self.index]
			self.stack[self.index] = None
			return val
		else:
			return None
	def resize(self,capacity):
		temp = [None]*capacity
		for i,obj in enumerate(self.stack):
			if obj ==None:
				break
			temp[i] = obj
		self.stack = temp
	
	def isEmpty(self):
		if (index==0):
			return True
		else:
			return False
	def size(self):
		return len(self.stack)
		
if __name__ == "__main__":
	stack = arrayStack()

	stack.push(13)
	stack.push(13)
	stack.push(13)
	stack.push(13)
	stack.push(13)
	#print(stack.size())
	stack.pop()
	stack.pop()
	stack.pop()
	stack.pop()
	print(stack.size())
	print(stack.pop())
	print(stack.pop())