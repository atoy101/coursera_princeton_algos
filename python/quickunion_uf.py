#Union-Find quickunion implementation
#author: Alex Toy
#date: 9/24/2021

import sys

class QuickunionUF:

	def __init__(self, N):		#O(n) time
		self.data = []
		self.weight = []
		self.max = []
		for i in range(N):
			self.data.append(i)
			self.weight.append(1)
			self.max.append(i)
	
	def root(self, i):
		original=i
		while(self.data[i]!=i):
			self.data[i]=self.data[self.data[i]]
			i= self.data[i]
		return i
	
	def find(self,i):
		i = self.root(i)
		return self.max[i]
		
	def union(self,num1,num2):		#O(1) time
		i = self.root(num1)
		j = self.root(num2)
		if num1>num2:
			max=num1
		else:
			max=num2
		
		if (i==j):
			return
		if (self.weight[i]>self.weight[j]):
			self.data[j]=i
			self.weight[i]+=self.weight[j]
			if self.max[i] < max:
				self.max[i]=max
		else:
			self.data[i]=j
			self.weight[j]+=self.weight[i]
			if self.max[j] < max:
				self.max[j]=max
			
	def connected(self,num1,num2):		#O(n) 
		return self.root(num1) == self.root(num2)
			
	def print_data(self):		#O(n) time
		for i in range(len(self.data)):
			print(str(i)+","+str(self.data[i])+","+str(self.weight[i])+","+str(self.max[i]))
			
			

if __name__ == "__main__":
	
	x= QuickunionUF(10)
	x.union(2,6)
	x.union(6,1)
	x.union(1,9)
	x.union(5,2)
	print(x.find(5))
	print(x.find(2))
	print(x.find(6))
	print(x.find(9))
	x.print_data()
	#y = x.connected(2,100000)
	#print(y)
	