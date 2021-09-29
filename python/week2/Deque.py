#double-ended queue doubly linked list implementation
#author: Alex Toy
#date: 9/29/21

class Deque:
	def __init__(self):
		self.first = None
		self.last = None
		self.numitems = 0
		
	def isEmpty(self):
		return self.numitems==0
	def size(self):
		return self.numitems
		
	def addFirst(self,val):
		if (self.numitems==0):
			self.first = self.Node(val)
			self.last = self.first
		else:
			oldfirst = self.first
			self.first = self.Node(val)
			self.first.prev = oldfirst
			oldfirst.next = self.first
		self.numitems+=1
	def addLast(self,val):
		if (self.numitems==0):
			self.last = self.Node(val)
			self.first = self.last
		else:
			oldlast = self.last
			self.last = self.Node(val)
			self.last.next = oldlast
			oldlast.prev = self.last
		self.numitems+=1
	def removeFirst(self):
		if (self.isEmpty()):
			return None
		elif (self.numitems==1):
			val = self.first.val
			self.first = None
			self.last = None
			self.numitems-=1
			return val
		else:
			val = self.first.val
			self.first = self.first.prev
			self.first.next = None
			self.numitems-=1
			return val
			
	def removeLast(self):
		if (self.isEmpty()):
			return None
		elif (self.numitems==1):
			val = self.last.val
			self.last = None
			self.first = None
			self.numitems-=1
			return val
		else:
			val = self.last.val
			self.last = self.last.next
			self.last.prev = None
			self.numitems-=1
			return val
	
	class Node:
		def __init__(self, val):
			self.val = val
			self.next = None
			self.prev = None
			
if __name__ == "__main__":
	q = Deque()
	q.addLast(1)
	q.addFirst(2)
	print(q.removeLast())
	print(q.removeFirst())
	q.addLast(3)
	print(q.removeFirst())
	print(q.removeFirst())
	q.addLast(1)
	q.addLast(2)
	q.addLast(3)
	q.addLast(4)
	print(q.removeFirst())
	print(q.removeLast())
	