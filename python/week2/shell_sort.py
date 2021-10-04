#Shell sort
#Author: Alex Toy
#Date: 9/30/21
import random
def shellsort(array):
	h=1
	while(h<len(array)):
		h = (h*3)+1
	
	while(h>0):
		for i in range(h,len(array),h):
			j=i
			while(j-h>=0):
				if (array[j]<array[j-h]):
					array[j],array[j-h]=array[j-h],array[j]
				j-=h
		print(array)
		h//=3
		
		
if __name__=="__main__":
	array=[]
	for i in range(100,0,-1):
		array.append(i)
	print(array)
	shellsort(array)
	print(array)
			
			