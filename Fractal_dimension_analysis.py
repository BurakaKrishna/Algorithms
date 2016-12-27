print 'Finding the fractal dimension of the matrix'
import numpy as np
import matplotlib.pyplot as plt
path = '/Users/apple/DLA_py/point_attractor/Single_point_Grid_of_200_with_points5000_and_stickiness_0.05_2016-12-27Matrix.txt'
rows = np.loadtxt(path)

plt.imshow(np.asmatrix(rows), cmap = 'prism')
plt.show()
# Matrix size reduction
rows = rows[~np.all(rows == 0, axis=1)]
rows = rows[:,rows.sum(axis=0)>=1]
size = max(rows.shape)
m = int(np.log(size)/np.log(2))
plt.matshow(rows, cmap = plt.cm.binary)
plt.show()

def Fractal_dimensional_analysis(m,rows):
	cnts = []
	for lev in range(m):
		block_size = 2**lev
		cnt = 0
		for j in range(int(size/(2*block_size))):
			for i in range(int(size/block_size)):
				cnt = cnt + rows[j*block_size:(j+1)*block_size, i*block_size:(i+1)*block_size].any()
		cnts.append(cnt)
	data = np.array([(2**(m-(k+1)),cnts[k]) for k in range(m)])
	print data
	non_zeros = len(np.trim_zeros(data[:,1]))
	xs = np.log(data[:,0][:non_zeros])
	ys = np.log(data[:,1][:non_zeros])
	xs = xs[1:]
	ys = ys[1:]
	A = np.vstack([xs, np.ones(len(xs))]).T
	m,b = np.linalg.lstsq(A, ys)[0]
	def line(x): return m*x+b
	ys = line(xs)
	plt.plot(xs,ys)
	print 'The fractal dimension fo the matrix is %s' %m

Fractal_dimensional_analysis(m,rows)