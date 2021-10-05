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
			return True
		elif self.x>other.x:
			return False
		elif self.y<other.y:
			return True
		elif self.y>other.y:
			return False
		else:
			return 0
	def __gt__(self,other):
		if self.x<other.x:
			return False
		elif self.x>other.x:
			return True
		elif self.y<other.y:
			return False
		elif self.y>other.y:
			return True
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
	if len(sys.argv) > 1:
		with open(sys.argv[1], 'r') as file:
			num_points = int(file.readline())
			for line in file:
				p = line
				p=p.split()
				points.append(Point(int(p[0]),int(p[1])))
	else: 
		print("need input")
		exit()
	
	plot_points(points)
	lines = []
	
	for p in points:
		cmp_key = cmp_to_key(p.cmp_slopes)
		sorted_p = sorted(points,key=cmp_key)		#sort points by slope compared to point p
		sorted_p.remove(p)							#remove the origin from the sorted list
		origin = p
		count=1
		prev_slope=None
		temp_points=[]
		slopes =[]
		
		for i,q in enumerate(sorted_p):				#if 3 same slopes in a row, add them all to a list, sort by (x,y) and take the furthest apart
			slope=p.slopeto(q)
			slopes.append(slope)
			if slope==prev_slope:
				count+=1
				temp_points.append(q)
			if slope!=prev_slope or i==len(sorted_p)-1:
				if count>=3:	
					temp_points.append(origin)
					temp_points.sort()
					temp_point = [temp_points[0],temp_points[-1]]
					print(temp_points,"temp points")
					if  temp_point in lines:
						pass
					else:
						lines.append(temp_point)
				count = 1
				temp_points=[]
			prev_slope=slope
			temp_points.append(q)

	
	#print(lines)
	for line in lines:
		plot_lines(line)
	plt.show()