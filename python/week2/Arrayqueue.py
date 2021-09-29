#array implementation of a queue
#author: Alex Toy
#date: 9/29/21

class arrayQueue:
	def __init__(self):
		self.data = [None]*1
		self.first = 0
		self.last = 0
		
	def enqueue(self, val):
		if (self.last>0 and self.last==len(self.data)):
			self.resize(len(self.data)*2)
		self.data[self.last] = val
		self.last+=1
	
	def dequeue(self):
		if (self.first==self.last):
			return None
		if ((self.last-self.first)<=int(len(self.data)/4)):
			self.resize(int(len(self.data)/2))
		val = self.data[self.first]
		self.data[self.first] = None
		self.first+=1
		return val
		
	def resize(self,capacity):
		temp = [None]*capacity
		last = 0
		self.first =0
		index = 0
		for obj in self.data:
			if obj==None:
				continue
			temp[index] = obj
			index+=1
		self.last = index
		self.data = temp
		
	def size(self):
		return len(self.data)
	def printq(self):
		print(self.data)

if __name__ == "__main__":
	q = arrayQueue()
	for i in range(100):
		q.enqueue(i)
		if i%2==0:
			x= q.dequeue()
		print(x)
		q.printq()
	
	