#mergesort, iterative and recursive 
#author: Alex Toy
#date: 10/1/21

import random
def mergesort_recusive(array,lo,hi):
	aux = []
	for i in range(len(array)):
		aux.append(array[i])
	sort(array,aux,lo,hi)
	
def mergesort_iterative(array):
	aux = []
	for i in range(len(array)):
		aux.append(array[i])
	for sz in range_double(1,len(array)):
		lo = 0
		while (lo<len(array)-sz):
			merge(array,aux,lo,lo+sz-1,min(lo+sz+sz-1,len(array)-1))
			lo+=sz+sz
			
#merge takes 1 array with 2 sorted halves, lo-mid and mid+1-high, and 'merges'
#the two halves into one fully sorted array
def merge(array,aux,lo,mid,hi):
	for i in range(lo,hi+1):
		aux[i]=array[i]
	k=lo
	j = mid+1
	for i in range(lo,hi+1):
		if k>mid:
			array[i]=aux[j]
			j+=1
		elif j>hi:
			array[i]=aux[k]
			k+=1
		elif aux[j]<aux[k]:
			array[i] = aux[j]
			j+=1
		else:
			array[i] = aux[k]
			k+=1
	
def sort(array,aux,lo,hi):
	if (hi<=lo):
		return inv_count
	mid = int(lo + (hi-lo)/2)
	sort(array,aux,lo,mid)
	sort(array,aux,mid+1,hi)
	merge(array,aux,lo,mid,hi)
	
def range_double(start,stop):
	i = start
	while i<stop:
		yield i
		i+=i

if __name__ == "__main__":
	array = []
	for i in range(5,0,-1):
		array.append(i)#random.randint(0,100))
	print(array)
	mergesort_iterative(array)
	print(array)