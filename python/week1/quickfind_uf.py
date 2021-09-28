#Union-Find quickfind implementation
#author: Alex Toy
#date: 9/24/2021

import sys

class QuickfindUF:

	def __init__(self, N):		#O(n) time
		self.data = []
		for i in range(N):
			self.data.append(i);
			
	def union(self,num1,num2):		#O(n) time
		id = self.data[num1]
		for i in range(len(self.data)):
			if self.data[i]==id:
				self.data[i]= self.data[num2];
			
	def connected(self,num1,num2):		#O(1) time
		if (self.data[num1] == self.data[num2]):
			return True;
		else:
			return False;
			
	def print_data(self):		#O(n) time
		for i in range(len(self.data)):
			print(str(i)+","+str(self.data[i]))
			

if __name__ == "__main__":
	
	x= QuickfindUF(10)
	x.union(0,1)
	x.union(7,8)
	x.union(1,8)
	x.print_data()
	y = x.connected(0,1)
	print(y)
	