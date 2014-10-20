import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot(algorithm, dim, porder):
	cnt = 11
	
	fig, ax = plt.subplots()

	for i in [2,4,8,16,32,64,128]:
		fr = open("./statistic-%s/dim%sporder%sgrow%d.txt" % (algorithm,dim,porder,i),"r")
	
		x = []
		y = []
		tmp = 1
	
		for line in fr.readlines():
			arr = line.strip().split()
			if tmp >= cnt: break
			x.append(eval(arr[0]))
			y.append(eval(arr[2]))
			tmp = tmp + 1

		fr.close()

		N = len(x)
		ind = np.arange(N)

		ax.plot(ind, y,'o-',label='grow = %d' % i)

	def format(indx, pos=None):
		thisind = np.clip(int(indx),0,N-1)
		return x[thisind]

	ax.xaxis.set_ticks([0.0,1.0,9.0])
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(format))
	fig.autofmt_xdate()
	plt.title('spread timepass\n %s dim = %s porder = %s' % (algorithm,dim,porder))
	plt.xlabel('number of particles')
	plt.ylabel('timepass (ms)')
	plt.legend(loc = 'upper left')
	#plt.show()
	fig.savefig('./figure/plotGrow*-%s-dim%s-porder%s.png' % (algorithm,dim,porder))
