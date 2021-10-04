#selection sort implementation 
#O(n^2/2) instructions O(n)swaps
#Author: Alex Toy
#Date: 9/29/21
import random
def selectionSort(array):
	for i,obji in enumerate(array):
		min=obji
		min_index = i
		for j,objj in enumerate(array[i:],start=i):
			if (objj<min):
				min=objj
				min_index=j
		if (min<obji):
			array[i],array[min_index] = array[min_index],array[i]

if __name__=="__main__":
	array = []
	for i in range(5):
		array.append(random.randint(0,100))
	selectionSort(array)
	print(array)