#Union-Find quickunion implementation
#author: Alex Toy
#date: 9/24/2021

import sys

class QuickunionUF:

	def __init__(self, N):		#O(n) time
		self.data = []
		self.weight = []
		for i in range(N):
			self.data.append(i)
			self.weight.append(1)
	
	def root(self, i):
		while(self.data[i]!=i):
			self.data[i]=self.data[self.data[i]]
			i= self.data[i]
		return i
		
	def union(self,num1,num2):		#O(1) time
		i = self.root(num1)
		j = self.root(num2)
		if (i==j):
			return
		if (self.weight[i]>self.weight[j]):
			self.data[j]=i
			self.weight[i]+=self.weight[j]
		else:
			self.data[i]=j
			self.weight[j]+=self.weight[i]
			
	def connected(self,num1,num2):		#O(n) 
		return self.root(num1) == self.root(num2)
			
	def print_data(self):		#O(n) time
		for i in range(len(self.data)):
			print(str(i)+","+str(self.data[i])+","+str(self.weight[i]))
			
			

if __name__ == "__main__":
	
	x= QuickunionUF(1000000)
	for i in range(1000000):
		if i%2==0:
			x.union(i,i+1)
	for i in range(1000000):
		if i%5==0:
			x.union(i,i+3)
	x.print_data()
	y = x.connected(2,100000)
	print(y)
	