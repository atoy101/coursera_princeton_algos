#heapsort
#author: Alex Toy
#date: 10/7/21

import random

def heapsort(array):
	for i in range(len(array)-1,-1,-1):
		if (i*2) > len(array)-1:
			continue
		else:
			sink(array,i,len(array))
			
	for i in range(len(array)-1,0,-1):
		array[0],array[i]=array[i],array[0]
		sink(array,0,i)

def sink(array,k,length):
	
	if (k*2)+1>=length:
		if array[k]<array[k*2]:
			array[k],array[k*2] = array[k*2],array[k]
		return
		
	while(array[k]<array[2*k] or array[k]<array[(2*k)+1]):
		if array[(k*2)+1]<array[2*k]:
			array[k],array[2*k] = array[2*k],array[k]
			k*=2
		else:
			array[k],array[(2*k)+1] = array[(2*k)+1],array[k]
			k=(2*k)+1
		if (2*k)+1>=length:
			break


if __name__ == "__main__":
	array = []
	for i in range(10):
		array.append(i)
	heapsort(array)
	print(array)