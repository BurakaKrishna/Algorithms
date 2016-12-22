import random as rd
import matplotlib.pyplot as plt
import numpy as np
import time
import csv

class dla(object):
	def __init__(self, N, m):
		self.size = N
		self.arena = [[0 for i in xrange(N)] for j in xrange(N)]
		self.arena[N/2][N/2] = 1
		self.particles = m
	
	def start(self, edge):
		while(True):
			x = rd.randint(0,N-1)
			if(edge==0 and self.arena[x][0]==0):
				return (x,0)
			elif(edge==1 and self.arena[0][x]==0):
				return (0,x)
			elif(edge==2 and self.arena[x][N-1]==0):
				return (x,N-1)
			elif(edge==3 and self.arena[N-1][x]==0):
				return (N-1,x)
	
	def neighbours(self, pos):
		l = [(pos[0], (pos[1]-1)%N), ((pos[0]-1)%N, pos[1]), (pos[0], (pos[1]+1)%N), ((pos[0]+1)%N, pos[1])]
		return l
	
	def walk(self, seed):
			while(True):
			ney = self.neighbours(seed)
			for x in ney:
				if(self.arena[x[0]][x[1]]>0):
					if rd.uniform(0,1) < 0.1:
						self.arena[seed[0]][seed[1]] = 1
						self.particles -= 1
						return seed
			seed = ney[rd.randint(0,len(ney)-1)]
	
	def simulate(self):
		while(self.particles>0):
			t0 = time.time()
			edge = rd.randint(0,3)
			seed = self.start(edge)
			print self.particles
			seed = self.walk(seed)
			u = time.time()-t0
			t.append(u)
			data.writerow([m-self.particles, u, seed[0], seed[1]])
	

t = []
N = 10
m = 10

import datetime
path = '%s times.csv' % datetime.datetime.now().date()
output = open(path, 'w+')
data = csv.writer(output)
data.writerow(['Particle#', 'Stick Time', 'Row', 'Column'])

model = dla(N, m)
model.simulate()
print 'Finished simulating'
print model.arena

plt.imshow(np.asmatrix(model.arena), cmap = 'prism')
plt.show()

plt.plot(range(1, len(t)+1), t)
plt.show()
