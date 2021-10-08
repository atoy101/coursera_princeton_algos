#min priority queue implementation with binary heap using an array
#author: Alex Toy
#date: 10/7/21
import random
class minQueue:
	def __init__(self):
		self.array = [None]*2
		self.index = 1
	
	def resize(self,capacity):
		temp = [None]*capacity
		for i in range(len(self.array)):
			if i==0:
				continue
			if self.array[i] == None:
				break
			temp[i] = self.array[i]
		self.array = temp
	
	def delmin(self):
		if (self.index == len(self.array)//4):
			self.resize(len(self.array)//2)
			
		min = self.array[1]
		self.array[1],self.array[self.index-1] = self.array[self.index-1],self.array[1]
		self.array[self.index-1] = None
		if (self.index>1):
			self.index-=1
		if self.index>2:
			self.sink(1)
		return min
	def min(self):
		return self.array[1]
	def insert(self,val):
		if (self.index > 0 and self.index == len(self.array)):
			self.resize(len(self.array)*2)
		self.array[self.index] = val
		self.swim(self.index)
		self.index+=1
	
	def swim(self,k):
		while(k>1 and self.array[k]<self.array[k//2]):
			self.array[k],self.array[k//2] = self.array[k//2],self.array[k]
			k//=2
		
	
	def sink(self,k):
		
		if (k*2)+1>=self.index:
			if self.array[k]>self.array[k*2]:
				self.array[k],self.array[k*2] = self.array[k*2],self.array[k]
			return
			
		while(self.array[k]>self.array[k*2] or self.array[k]>self.array[(k*2)+1]):
			if self.array[k*2] < self.array[(k*2)+1]:
				self.array[k],self.array[k*2] = self.array[k*2],self.array[k]
				k*=2
			else:
				self.array[k],self.array[(k*2)+1] = self.array[(k*2)+1],self.array[k]
				k=(k*2)+1
			if (k*2)+1>=self.index:
				break
				
	def __str__(self):
		return str(self.array)
			
if __name__=="__main__":
	q = minQueue()
	for i in range(100000):
		x =random.randint(0,10)
		q.insert(x)

	array = []
	x= q.delmin()
	while(x!=None):
		array.append(x)
		x = q.delmin()
	print(array)
	print(len(array))

