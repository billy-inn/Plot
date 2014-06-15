#plot a simple figure of nearest-neighbor coupled network
#input N and K as commanded
#gurantee that K<N and K is even

from numpy import *
import matplotlib.pyplot as plt

def plot():
	N = input('please enter the total number of nodes:')
	K = input("please enter the number of each node's neighbors:")
	if (K > N-1) or (K%2 == 1):
		print 'error: K must no larger than N-1 and be even'
		return
	angle = arange(0,2*pi,2*pi/N)
	x = 100*sin(angle)
	y = 100*cos(angle)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	#plot the nodes
	ax.scatter(x,y,s=6,c='r')
	#calculate the adjacency matrix
	A = zeros((N,N))
	for i in range(N):
		for j in range(i+1,i+K/2):
			jj = j
			if jj >= N: jj %= N
			A[i,jj] = 1; A[jj,i] = 1
	#plot the edges
	for i in range(N):
		for j in range(i+1,N):
			if A[i,j] == 1:
				ax.plot([x[i],x[j]],[y[i],y[j]],'b')
	plt.show()

