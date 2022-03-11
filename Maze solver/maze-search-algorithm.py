#first thing is the node data storing one to store the state, parent, action underwent 
import sys
class Node() :
	def __init__(self, state, parent, action) :
		self.state=state
		self.parent=parent
		self.action=action

#class for the frontier to store nodes those are objects of the class node
#we can use frontier as Stack or we can use frontier as queue which depends on the approach of #algorithm to that specific problem. we can use queue as frontier by changing the intake and output #of array at function in remove function of the below one
#if  we use frontier as stack then breadth first search else if we use queue we call that approach as #depth first search or vice versa check the referenece.
class StackFrontier() :
	def __init__(self) :
		self.frontier=[]
	def add(self, node) :
		self.frontier.append(node)
	def contains_state(self, state) :
		#print(any(node.state == state for node in self.frontier))
		return any(node.state == state for node in self.frontier)
	def empty(self) :
		#print(len(self.frontier))
		return len(self.frontier)==0
	def remove(self) :
		if self.empty():
			raise Exception('frontier empty')
		else :
			node =self.frontier[-1]
			self.frontier=self.frontier[:-1]
			return node
#now we will build a class of maze with diff funtionality and diff stuff so lets dive deep into this part of code to get exciting results at

class Maze() :
	def __init__(self, filename) :
		with open(filename) as f:
			self.contents=f.read()
		if self.contents.count('A')!=1 :
			raise Exception('the maze or play should only have single start point')
		elif self.contents.count('B')!=1 :
			raise Exception('the maze or play should only have single goal point')
		self.contents =self.contents.splitlines()

	#measuring dimensions of the maze

		self.height=len(self.contents)
		self.width=max(len(lines) for lines in self.contents)
		#print(self.height)
	#keeping track of the walls of the maze

		self.walls=[]
		for i in range(self.height) :
			rows=[]
			for j in range(self.width) :
				try:
					if self.contents[i][j] =='A' :
						self.start=(i,j)
						rows.append(False)
					elif self.contents[i][j] =='B' :
						rows.append(False)
						self.goal=(i,j)
					elif self.contents[i][j] ==' ' :
						rows.append(False)
					else :
						rows.append(True)
				except IndexError :
					rows.append(False)
			self.walls.append(rows)
		self.solution=None

#now we shall define a new funtion with the name print as we already created the last class of this problem

	def print(self) :
		solution =self.solution[1] if self.solution is not None else None
		for i, row in enumerate(self.walls) :
			for j, col in enumerate(row) :
				if (i,j) == self.start :
					print('A', end='')
				elif (i,j)==self.goal :
					print('B', end='')
				elif col :
					print('W', end='')
				elif solution is not None and (i,j) in solution :
					print('*', end='')
				else :
					print(' ', end='')
			print()
		print()

#lets define a new funtion of solving a maze

	def neighbour(self, state) :
		row, col =state
		choice=[('up', (row-1,col)),
		             ('down', (row+1,col)),
		             ('left', (row,col-1)),
		             ('right', (row,col+1))]
		result=[]
		for action,(r,c) in choice :
#here c in the code means maze wall
			if 0<=r<self.height and 0<=c<self.width and self.contents[r][c]!='c' and (not(r==0 and c==0)) :
				result.append((action,(r,c)))
		#print(result)
		return result

#lets define a final funtion to calc the maze problem

	def solve(self) :
		start=Node(state=self.start, parent=None, action=None)
		frontier=StackFrontier()
		frontier.add(start)
		no_explored=0
		self.explored_set=[]
		while True:
			if frontier.empty():
				raise Exception('No solution')
			node =frontier.remove()
			no_explored+=1
			self.explored_set.append(node.state)
			#print(self.explored_set[0])
			if node.state==self.goal :
				cells=[]
				actions=[]
				while node.parent is not None:		
					actions.append(node.action)
					cells.append(node.state)
					node=node.parent
				actions.reverse()
				cells.reverse()
				self.solution=(actions,cells)
				#print(self.solution)
				return	

		#add nodes to frontier

			for action, state in self.neighbour(node.state) :
				if not frontier.contains_state(state) and state not in self.explored_set :
					child=Node(state=state, parent=node, action=action)			
					frontier.add(child)
					#print('node added')
	def output_image(self) :
		from PIL import Image, ImageDraw
		cell_size=50
		cell_border=2
		img=Image.new('RGBA', (self.width*cell_size, self.height*cell_size), 'black')
		draw =ImageDraw.Draw(img)
		solution=self.solution[1] if self.solution is not None else None
		for i, row in enumerate(self.walls) :
			for j, col in enumerate(row) :
				if col:
					fill = (40, 40, 40)
				elif (i,j)==self.start :
					fill = (255, 0, 0)
				elif (i,j)==self.goal :
					fill= (0, 171, 28)
				elif solution is not None and (i,j) in solution :
					fill = (220, 235, 113)
				elif solution is not None and (i,j) in self.explored_set:
					fill = (212, 97, 85)
				else :
					fill=(237, 240, 252)
				draw.rectangle(([(j * cell_size + cell_border, i * cell_size + cell_border),((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]), fill=fill)
			img.save('graphical_maze.png')
ob=Maze('maze file to test search algorithm.txt')#or we can give sys.argv[1] to accept name of file #from terminal window while python maze.py maze.txt
ob.solve()
ob.print()
ob.output_image()
	

				
	