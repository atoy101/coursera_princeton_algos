#sliding puzzle solved using A* search
#author: Alex Toy
#date: 10/8/21
from min_queue import minQueue

class Board:
	#board is a int[][] n-by-n
	def __init__(self,board):
		self.board = board
		self.priority = 0
	def __lt__(self,other):
		if self.manhattan()+self.priority<other.manhattan()+other.priority:
			return True
		else:
			return False
				
	
	def toString(self):
		for row in self.board:
			print(row)
		return ""
	
	def dimension(self):
		return len(self.board)
	
	def hamming(self):
		hamming = 0
		index = 1
		for i in range(self.dimension()):
			for j in range(self.dimension()):
				if self.board[i][j] == index:
					pass
				elif i==self.dimension()-1 and j==self.dimension()-1:
					continue
					if self.board[i][j] != 0:
						hamming+=1
				else:
					hamming+=1
				index+=1
		return hamming
	
	def manhattan(self):
		manhattan = 0
		index = 1
		for i in range(self.dimension()):
			for j in range(self.dimension()):
				if self.board[i][j] == index:
					pass
				elif self.board[i][j] == 0:
					pass
					#manhattan += (self.dimension()-1)**2-(i+j)
				else:
					index_row = self.board[i][j]//self.dimension() + (self.board[i][j] % self.dimension() > 0) -1
					index_col = self.board[i][j]%self.dimension()-1
					if index_col<0:
						index_col =2
					man_temp = (index_row-i if (index_row-i)>0 else -(index_row-i)) + (index_col-j if (index_col-j)>0 else -(index_col-j))
					manhattan += man_temp
					man_temp=0
				index+=1
		return manhattan
	
	def isGoal(self):
		if self.hamming()==0:
			return True
		else:
			return False
	
	def equals(self,other):
		if other == None:
			return False
		if self.board==other.board:
			return True
		else:
			return False
	
	def neighbors(self):
		neighbors = []
		swaps = []
		empty = None
		for row in range(self.dimension()):
			for col in range(self.dimension()):
				if self.board[row][col]==0:
					empty = (row,col)
		swaps.append((empty[0]-1,empty[1]))
		swaps.append((empty[0]+1,empty[1]))
		swaps.append((empty[0],empty[1]+1))
		swaps.append((empty[0],empty[1]-1))
		for swap in swaps:
			temp_board = []
			for x in self.board:
				temp_board.append(x.copy())
			if swap[0]<0 or swap[0]>self.dimension()-1 or swap[1]<0 or swap[1]>self.dimension()-1:
				continue
			else:
				temp_board[empty[0]][empty[1]],temp_board[swap[0]][swap[1]] = temp_board[swap[0]][swap[1]],temp_board[empty[0]][empty[1]]
				t = Board(temp_board)
				yield t
			
class Solver:
	def __init__(self,board):
		self.board = board
		prev=None
		minQ = minQueue()
		self.num_moves = 0
		self.board.priority = self.num_moves
		minQ.insert(self.board)
		while(self.board.isGoal()==False):
			for neighbor in self.board.neighbors():
				neighbor.priority=self.board.priority+1
				if (neighbor.equals(prev)):
					pass
				else:
					minQ.insert(neighbor)
			min = minQ.delmin()
			prev=self.board
			self.board = min
		print(self.board.toString())
		print(self.board.priority)
			
			




if __name__=="__main__":
	b = Board([[8,6,7],[2,5,4],[3,0,1]])
	s = Solver(b)

	
	