import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

cnt = 9
limit = 20

for (i,j) in [(128,4)]:
	fig,ax = plt.subplots()
	bar_width = 0.35
	ind = np.arange(limit-cnt)
	print i,j

	fr = open("./statistic-naive/dim%dporder%dPhi0.1.txt" % (i,j),"r")
	
	x = []
	pre = []
	spread = []
	tmp = 0
	
	for line in fr.readlines():
		arr = line.strip().split()
		#if tmp > cnt: break
		if tmp < cnt: tmp = tmp+1;continue
		if tmp >= limit: break
		x.append(eval(arr[0]))
		pre.append(eval(arr[1]))
		spread.append(eval(arr[3]))
		tmp = tmp + 1

	fr.close()

	p1 = plt.bar(ind, pre, bar_width, color='r', hatch='x', label='Naive Precompution')
	p2 = plt.bar(ind, spread, bar_width, color='y', hatch='x', bottom=pre, label='Naive Spread')

	fr = open("./statistic-block/dim%dporder%dGrow64.txt" % (i,j),"r")

	pre = []
	spread = []
	tmp = 0

	for line in fr.readlines():
		arr = line.strip().split()
		#if tmp > cnt: break
		if tmp < cnt: tmp = tmp+1;continue
		if tmp >= limit: break
		pre.append(eval(arr[1]))
		spread.append(eval(arr[2]))
		tmp = tmp + 1
	fr.close()

	p3 = plt.bar(ind+bar_width, pre, bar_width, color='b', hatch='\\',label='GroupCSR Precompution')
	p4 = plt.bar(ind+bar_width, spread, bar_width, color='g', hatch='\\',bottom=pre, label='GroupCSR Spread')

	preList = []
	spreadList = []
	for thread in [1,2,4,8,16,32]:
		fr = open("./statistic-single/dim%dporder%dsthread%d.txt" % (i,j,thread),"r")
		pre = []
		spread = []
		tmp = 0
		for line in fr.readlines():
			arr = line.strip().split()
			if tmp > cnt: break
			#if tmp < cnt: tmp = tmp+1;continue
			#if tmp >= limit: break
			pre.append(eval(arr[1]))
			spread.append(eval(arr[2]))
			tmp = tmp + 1
		fr.close()
		preList.append(pre)
		spreadList.append(spread)
	
	pre = []
	spread = []
	
	for k in range(cnt+1):
		s = 1e10
		index = -1
		for p in range(6):
			if s > preList[p][k] + spreadList[p][k]:
				s = preList[p][k] + spreadList[p][k]
				index = p
		pre.append(preList[p][k])
		spread.append(spreadList[p][k])
	
	#p5 = plt.bar(ind+bar_width*2, pre, bar_width, color='grey',label='SingleCSR Precompution')
	#p6 = plt.bar(ind+bar_width*2, spread, bar_width, color='black', bottom=pre, label='SingleCSR Spread')

	plt.xticks(ind+bar_width,x)
	fig.autofmt_xdate()
	plt.title('precompution and spread timepass\n dim = %d porder = %d' % (i,j))
	plt.xlabel('number of particles')
	plt.ylabel('timepass (ms)')
	plt.legend(loc = 'upper left')
	plt.tight_layout()
	#plt.show()
	plt.savefig('./figure/plotBarh*-dim%d-porder%d.png' % (i,j))
