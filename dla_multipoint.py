import random as rd
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
import datetime

class walker(object):
	def __init__(self,pos,stuck):
		self.x = pos[0]
		self.y = pos[1]
		self.status = stuck
	
	def walk(self):
			ney = self.get_neighbours()
			pos = ney[rd.randint(0,len(ney)-1)]
			self.x,self.y = pos[0],pos[1]		
	
	def check_and_change_status(self,arena):
			for pos in self.get_neighbours():
				if(arena[pos[0]][pos[1]]>0):
					if rd.uniform(0,1) < stickiness:
						self.status = True
						break

	def get_neighbours(self):
			l = [(self.x, (self.y-1)%N), ((self.x-1)%N, self.y), (self.x, (self.y+1)%N), ((self.x+1)%N, self.y)]
			return l

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

def simulate(dla):
	for i in range(m):
		edge = rd.randint(0,3)
		walkers.append(walker(dla.start(edge),False))
	
	t0 = time.time()
	print 'The timer starts at %s' % t0
	while(dla.particles>0):
		for walker_bro in walkers:
			walker_bro.walk()
			walker_bro.check_and_change_status(dla.arena)
			if (walker_bro.status):
					dla.arena[walker_bro.x][walker_bro.y] = 1
					walkers.remove(walker_bro)
					dla.particles -= 1
					print 'The time we got a particle %s' % time.time()
					u = time.time()-t0
					t0 = time.time()
					print u
					t.append(u)
					# print t
					data.writerow([m-dla.particles, u, walker_bro.x, walker_bro.y])
					print len(walkers)

t = []
N = 500
m = 5000
stickiness = 1
path = 'Grid_of_%s_with_points%s_and_stickiness_%s_%s' % (N,m,stickiness,datetime.datetime.now().date())
output = open(path + '.csv', 'w+')
data = csv.writer(output)
data.writerow(['Particle#', 'Stick Time', 'Row', 'Column'])

# output = open('times.csv', 'w+')
# data = csv.writer(output)
# data.writerow(['Particle#', 'Stick Time', 'Row', 'Column'])
edge = rd.randint(0,3)
walkers = []
dla = dla(N, m)
# Walker = walker(dla.start(edge),False)
# print Walker.x,Walker.y,Walker.stuck
# while(Walker.stuck == False):
# 	print Walker.x,Walker.y,Walker.stuck
# 	Walker.walk()
# 	Walker.check_status(dla.arena)
# 	print Walker.x,Walker.y,Walker.stuck
simulate(dla)
np.save(path + 'Matrix.npy',np.asmatrix(dla.arena))
np.savetxt(path + 'Matrix.txt',np.asmatrix(dla.arena))
print 'Finished simulating'

plt.imshow(np.asmatrix(dla.arena), cmap = 'prism')
plt.show()
