import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot(algorithm, dim, porder):
	
	fig, ax = plt.subplots()

	for i in [1,2,4,8,16,32]:
		fr = open("./statistic-%s/dim%sporder%ssthread%d.txt" % (algorithm,dim,porder,i),"r")
	
		x = []
		y = []
		tmp = 1
	
		for line in fr.readlines():
			arr = line.strip().split()
			x.append(eval(arr[0]))
			y.append(eval(arr[2]))
			tmp = tmp + 1

		fr.close()

		N = len(x)
		ind = np.arange(N)

		ax.plot(ind, y,'o-',label='sthread = %d' % i)

	def format(indx, pos=None):
		thisind = np.clip(int(indx),0,N-1)
		return x[thisind]

	ax.xaxis.set_ticks([0.0,1.0,9.0,10.0,18.0,20.0])
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(format))
	fig.autofmt_xdate()
	plt.title('spread timepass\n %s dim = %s porder = %s' % (algorithm,dim,porder))
	plt.xlabel('number of particles')
	plt.ylabel('timepass (ms)')
	plt.legend(loc = 'upper left')
	#plt.show()
	fig.savefig('./figure/plotSingle-%s-dim%s-porder%s.png' % (algorithm,dim,porder))
