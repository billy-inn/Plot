import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot(algorithm, porder, phi):
	cnt = 22
	
	fig, ax = plt.subplots()

	for i in [32,64,128]:
		fr = open("./statistic-%s/dim%dporder%sPhi%s.txt" % (algorithm,i,porder,phi),"r")
	
		x = []
		y = []
		tmp = 1
	
		for line in fr.readlines():
			arr = line.strip().split()
			if tmp >= cnt: break
			x.append(eval(arr[0]))
			y.append(eval(arr[3]))
			tmp = tmp + 1

		fr.close()

		N = len(x)
		ind = np.arange(N)

		ax.plot(ind, y,'o-',label='dim = %d' % i)

	def format(indx, pos=None):
		thisind = np.clip(int(indx),0,N-1)
		return x[thisind]

	ax.xaxis.set_ticks([0.0,1.0,9.0,10.0,18.0,19.0,20.0])
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(format))
	fig.autofmt_xdate()
	plt.title('spread timepass\n %s porder = %s phi = %s' % (algorithm,porder,phi))
	plt.xlabel('number of particles')
	plt.ylabel('timepass (ms)')
	plt.legend(loc = 'upper left')
	#plt.show()
	fig.savefig('./figure/plotDim-%s-porder%s-phi%s.png' % (algorithm,porder,phi))
