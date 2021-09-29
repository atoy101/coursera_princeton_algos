#queue linked list implementation 
#author: alex toy
#date: 9/28/21

class LLqueue:
	def __init__(self):
		self.first = None
		self.last = None
	
	def __iter__(self):
		self.n = 0
		self.f = self.first
		return self
	
	def __next__(self):
		if (self.n==0):
			self.n+=1
			return self.f.val
		elif(self.f.next!=None):
			self.f= self.f.next
			return self.f.val
		else:
			raise StopIteration
	def isEmpty(self):
		return (self.first==None)
		
	def enqueue(self,val):
		oldlast = self.last
		self.last = self.Node(val)
		self.last.next = None
		if (self.isEmpty()):
			self.first = self.last
		else:
			oldlast.next = self.last
			
	def dequeue(self):
		val = self.first.val
		self.first = self.first.next
		if (self.isEmpty()):
			self.last = None
		return val
		
	
	class Node:
		def __init__(self,val):
			self.val = val
			self.next = None
	
	
if __name__=="__main__":
	queue= LLqueue()
	queue.enqueue(5)
	queue.enqueue(4)
	queue.enqueue(3)
	queue.enqueue(2)
	x = iter(queue)
	for y in x:
		print(y)