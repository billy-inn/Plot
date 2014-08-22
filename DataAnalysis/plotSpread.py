import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

cnt = 22


for (i,j) in [(32,4),(32,6),(64,4),(64,6)]:
	fig,ax = plt.subplots()

	fr = open("./statistic-naive/dim%dporder%dPhi0.1.txt" % (i,j),"r")
	
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

	ax.plot(ind, y,'o-',label='naive')

	fr = open("./statistic-matrix/dim%dporder%dPhi0.1.txt" % (i,j),"r")

	y = []
	tmp = 1

	for line in fr.readlines():
		arr = line.strip().split()
		if tmp >= cnt: break
		y.append(eval(arr[2]))
		tmp = tmp + 1
	fr.close()

	ax.plot(ind,y,'^-',label='matrix')

	fr = open("./statistic-gather/dim%dporder%dPhi0.1.txt" % (i,j),"r")

	y = []
	tmp = 1

	for line in fr.readlines():
		arr = line.strip().split()
		if tmp >= cnt: break
		y.append(eval(arr[3]))
		tmp = tmp + 1
	fr.close()

	ax.plot(ind,y,'v-',label='gather')

	def format(indx, pos=None):
		thisind = np.clip(int(indx),0,N-1)
		return x[thisind]

	ax.xaxis.set_ticks([0.0,1.0,9.0,10.0,18.0,19.0,20.0])
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(format))
	fig.autofmt_xdate()
	plt.title('spread timepass\n dim = %d porder = %d' % (i,j))
	plt.xlabel('number of particles')
	plt.ylabel('timepass (ms)')
	plt.legend(loc = 'upper left')
	#plt.show()
	plt.savefig('./figure/plotSpread-dim%d-porder%d.png' % (i,j))
