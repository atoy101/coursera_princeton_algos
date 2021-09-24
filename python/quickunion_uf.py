#Union-Find quickunion implementation
#author: Alex Toy
#date: 9/24/2021

import sys

class QuickunionUF:

	def __init__(self, N):		#O(n) time
		self.data = []
		for i in range(N):
			self.data.append(i);
			
	def union(self,num1,num2):		#O(1) time
		self.data[num1] = num2;
			
	def connected(self,num1,num2):		#O(n) time worst case from O(2n) by adding if statement to check if head==num1 or num2 
		next = self.data[num1]
		head = num1;
		while(head!=next):
			head = next
			next = self.data[head]
			if (head==num2):
				return True
		num1_root=head
		
		next = self.data[num2]
		head = num2;
		while(head!=next):
			head = next
			next = self.data[head]
			if (head==num1):
				return True
		num2_root=head;
		
		if (num2_root==num1_root):
			return True;
		else:
			return False;
			
	def print_data(self):		#O(n) time
		for i in range(len(self.data)):
			print(str(i)+","+str(self.data[i]))
			

if __name__ == "__main__":
	
	x= QuickunionUF(10)
	x.union(0,1)
	x.union(7,8)
	x.union(1,8)
	x.union(4,1)
	x.print_data()
	y = x.connected(7,4)
	print(y)
	