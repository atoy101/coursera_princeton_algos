#collinear points
#author:alex toy
#date: 10/4/21

import matplotlib.pyplot as plt
from functools import cmp_to_key
import sys

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def __lt__(self,other):
		if self.x<other.x:
			return 1
		elif self.x>other.x:
			return -1
		elif self.y<other.y:
			return 1
		elif self.y>other.y:
			return -1
		else:
			return 0
	def __gt__(self,other):
		if self.x<other.x:
			return -1
		elif self.x>other.x:
			return 1
		elif self.y<other.y:
			return -1
		elif self.y>other.y:
			return 1
		else:
			return 0
			
	def __eq__(self,other):
		if (self.x==other.x) and (self.y==other.y):
			return 1
		else:
			return 0
			
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"
		
	def __repr__(self):
		return "("+str(self.x)+","+str(self.y)+")"
		
	def slopeto(self,other):
		if other.x-self.x == 0:
			return float("inf")
		return (other.y-self.y)/(other.x-self.x)
	
	def cmp_slopes(self,p,q):
		if self.slopeto(p)<self.slopeto(q):
			return 1
		elif self.slopeto(p)>self.slopeto(q):
			return -1
		else:
			return 0
		
def plot_points(array):
	x=[]
	y=[]
	for p in array:
		x.append(p.x)
		y.append(p.y)
	plt.scatter(x,y)

def plot_lines(array):
	x=[]
	y=[]
	for p in array:
		x.append(p.x)
		y.append(p.y)
	plt.plot(x,y)



if __name__=="__main__":
	num_points = 0
	points = []
	if len(sys.argv) >= 1:
		with open(sys.argv[1], 'r') as file:
			num_points = int(file.readline())
			for line in file:
				p = line
				p=p.split()
				points.append(Point(int(p[0]),int(p[1])))
	else: 
		print("need input")
	
	plot_points(points)
	lines = []
	for p in points:
		cmp_key = cmp_to_key(p.cmp_slopes)
		sorted_p = sorted(points,key=cmp_key)
		sorted_p=sorted_p[1:]
		count=1
		prev_slope=None
		temp_points=[]
		for i,q in enumerate(sorted_p):
			slope=p.slopeto(q)
			if slope==prev_slope:
				count+=1
				temp_points.append(q)
			if slope!=prev_slope:
				if count>=2:
					print(temp_points)
					temp_points=sorted(temp_points)
					print(temp_points)
					print()
					temp_point = [temp_points[0],temp_points[-1]]
					if  temp_point in lines:
						pass
					else:
						#lines.append([p,sorted_p[i-1]])
						lines.append(temp_point)
				count = 1
				temp_points=[]
			prev_slope=slope
			temp_points.append(q)
	
	#print(lines)
	for line in lines:
		plot_lines(line)
	plt.show()