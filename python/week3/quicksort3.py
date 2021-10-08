#Dijkstra's 3way partitioning quicksort
#author: alex toy
#date: 10/6/21

def quicksort(array,lo,hi):
	if (hi<=lo):
		return;
	lt = lo
	i = lt+1
	gt=hi
	
	while(i<=gt):
		if (array[i]<array[lt]):
			array[i],array[lt]=array[lt],array[i]
			i+=1
			lt+=1
		elif (array[i]>array[lt]):
			array[i],array[gt]=array[gt],array[i]
			gt-=1
		else:
			i+=1
	
	quicksort(array,lo,lt-1)
	quicksort(array,gt+1,hi)
	
	
if __name__ == "__main__":
	array=[]
	for i in range(10):
		array.append(5)
	for i in range(10):
		array.append(i)
	print(array)
	quicksort(array,0,len(array)-1)
	print(array)