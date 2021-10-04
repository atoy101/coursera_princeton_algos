#Fisher-Yates (knuth) shuffle
#author: Alex Toy
#date: 9/30/21

import random
def knuthShuffle(array):
	for i, obj in enumerate(array):
		j=random.randint(0,i)
		array[i],array[j]=array[j],array[i]
		
if __name__=="__main__":
	array=[]
	for i in range(100):
		array.append(i)
	knuthShuffle(array)
	print(array)