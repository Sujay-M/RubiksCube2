import numpy as np

class RubiksCube:

#cubes is not required i guess
	def __init__(self,n):
		
		self.n = n
		self.faces = np.empty((6,n,n),dtype=int)
		self.no_cubes = n*n+(2*n+2*(n-2))*n-2
		self.initializeCube()

	def initializeCube(self):
		n = self.n
		for i in xrange(6):
			self.faces[i,:,:] = i
		self.cubes = np.lib.pad(np.zeros((n-2,n-2,n-2),dtype=int),1,'constant',constant_values=(1))
		count = 1
		for i in xrange(n):
			for j in xrange(n):
				for k in xrange(n):
					if self.cubes[i][j][k]==1:
						self.cubes[i][j][k] = count
						count+=1

	def leftRotate(self,index,direction):

		n = self.n
		#left is 2 and right is 3, direction = 1 is counterclockwise direction = 3 is clockwise
		if (index==0 or index==n-1):
			face = 2 if index==0 else 3
			self.faces[face][:] = np.rot90(self.faces[face],direction)

		up = self.faces[4]
		front = self.faces[0]
		down = self.faces[5]
		back = self.faces[1]
		temp = np.empty((n),dtype=int)	
		
		if (index!=n-1 and direction==1) or (index==n-1 and direction==3):
			#front - up - back - down
			temp[:] = up[:,index]
			up[:,index] = front[:,index]
			front[:,index] = down[:,index]
			down[:,index] = back[:,n-index-1]
			back[:,n-index-1] = temp[:]			

		else:			
			#up - front - down to back
			temp[:] = up[:,index]
			up[:,index] = back[:,n-index-1]
			back[:,n-index-1] = down[:,index]
			down[:,index] = front[:,index]
			front[:,index] = temp[:]


	def upRotate(self,index,direction):

		n = self.n
		#up is 4 and down is 5, direction = 1 is counterclockwise direction = 3 is clockwise
		if (index==0 or index==n-1):
			face = 4 if index==0 else 5
			self.faces[face][:] = np.rot90(self.faces[face],direction)
		
		front = self.faces[0]
		back = self.faces[1]
		left = self.faces[2]
		right = self.faces[3]
		temp = np.empty((n),dtype=int)

		if (index!=n-1 and direction==1) or (index==n-1 and direction==3):
			#left - front - right - back
			temp[:] = front[index,:]
			front[index,:] = left[index,:]
			left[index,:] = back[index,:]
			back[index,:] = right[index,:]
			right[index,:] = temp[:]
		else:
			#front - left - back - right
			temp[:] = front[index,:]
			front[index,:] = right[index,:]
			right[index,:] = back[index,:]
			back[index,:] = left[index,:]
			left[index,:] = temp[:]

	def frontRotate(self,index,direction):
		n = self.n
		#front is 0 and back is 1, direction = 1 is counterclockwise direction = 3 is clockwise
		if (index==0 or index==n-1):
			face = 0 if index==0 else 1
			self.faces[face][:] = np.rot90(self.faces[face],direction)
		
		left = self.faces[2]
		right = self.faces[3]
		up = self.faces[4]
		down = self.faces[5]
		temp = np.empty((n),dtype=int)

		if (index!=n-1 and direction==1) or (index==n-1 and direction==3):
			#up - left - down - right			
			temp[:] = up[n-index-1,:]
			up[n-index-1,:] = right[:,index]
			right[:,index] = down[index,:]
			down[index,:] = left[:,n-index-1]
			left[:,n-index-1] = temp[:]
		else:
			#up -right - down - left			
			temp[:] = up[n-index-1,:]
			up[n-index-1,:] = left[:,n-index-1]
			left[:,n-index-1] = down[index,:]
			down[index,:] = right[:,index]
			right[:,index] = temp[:]

	def winCheck():
		None