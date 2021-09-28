#Percolation Simulation
#Author: Alex Toy
#Date: 9/27/21
from pprint import pprint
import random
class Percolation:
	def __init__(self,N):
		self.N=N
		self.data = []
		self.open = []
		self.index = [[] for z in range(N)]
		self.numopen =0
		self.weight = []
		self.max = []
		count=0
		for i in range(N):
			for j in range(N):
				self.data.append(count)
				self.max.append(count)
				self.index[i].append(count)
				count+=1
				self.open.append(0)
				self.weight.append(1)
		#pprint(self.index)
	
	def open_site(self,row,col):
		if (row>self.N-1 or row<0 or col>self.N-1 or col<0):
			return False
		i = self.index[row][col]
		if self.open[i]==0:
			self.open[i] = 1
			self.numopen+=1
		if (self.isOpen(row+1,col)):
			self.union(i,i+self.N)
		if (self.isOpen(row-1,col)):
			self.union(i,i-self.N)
		if (self.isOpen(row,col+1)):
			self.union(i,i+1)
		if (self.isOpen(row,col-1)):
			self.union(i,i-1)
			
	def isOpen(self,row,col):
		if (row>self.N-1 or row<0 or col>self.N-1 or col<0):
			return False
		i = self.index[row][col]
		if self.open[i]==1:
			return True
		else:
			return False
	
	def isFull(self,row,col):
		if (row>self.N-1 or row<0 or col>self.N-1 or col<0):
			return False
		i = self.index[row][col]
		if self.open[i]==0:
			return True
		else:
			return False
	
	def root(self, i):
		original=i
		while(self.data[i]!=i):
			self.data[i]=self.data[self.data[i]]
			i= self.data[i]
		return i
		
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
	
	def percolates(self):
		top_root = []
		for n in range(self.N):
			top_root.append(self.data[n])
		for n in range(len(self.data)-self.N,len(self.data)):
			if self.data[n] in top_root:
				return True
		
		return False
		
	def print_array(self):
		count=0
		
		for i in range(self.N):
			print('[',end="")
			for j in range(self.N):
				print(self.data[count],end=",")
				count+=1
			print(']')
			
		count=0
		for i in range(self.N):
			print('[',end="")
			for j in range(self.N):
				print(self.open[count],end=",")
				count+=1
			print(']')
		#print(self.numopen)
		#print(x.percolates())
		
if __name__ == "__main__":

	numopen_array = []
	sum = 0
	N=5
	for i in range(2500):
		x = Percolation(N)
		while(x.percolates()==False):
			x.open_site(random.randint(0,N-1),random.randint(0,N-1))
		numopen_array.append(x.numopen)
	for x in numopen_array:
		sum+=x
	pprint(numopen_array)
	print((sum/len(numopen_array))/(N*N))

			
			
			