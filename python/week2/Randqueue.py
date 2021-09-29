#randomized queue implemented with array stack
#author: Alex Toy
#date: 9/29/21
import random
class RandomizedQueue:
	
	def __init__(self):
		self.stack = [None]*1
		self.index = 0
		
	def __iter__(self):
		self.i = self.index
		self.s = self.stack
		return self
	def __next__(self):
		if self.i>0:
			self.i -=1
			rand = random.randint(0,self.i)
			val = self.s[rand]
			self.s[rand] = self.s[self.i]
			return val
		else:
			raise StopIteration
		
	def enqueue(self,val):
		if (self.index > 0 and self.index == len(self.stack)):
			self.resize(len(self.stack)*2)
		self.stack[self.index]= val
		self.index+=1
	
	def dequeue(self):
		if (self.index == len(self.stack)/4):
			self.resize(int(len(self.stack)/2))
		if (self.index > 0):
			self.index-=1
			rand = random.randint(0,self.index)
			val = self.stack[rand]
			self.stack[rand] = self.stack[self.index]
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
	stack = RandomizedQueue()
	for i in range(100):
		stack.enqueue(i)
	x= iter(stack)
	z= iter(stack)
	array = []
	array2 = []
	for y in x:
		array.append(y)
	for y in z:
		array2.append(y)
	print(array2)
	print(array)
	