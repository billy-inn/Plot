import matplotlib.pyplot as plt
import numpy as np

fig, (ax0,ax1) = plt.subplots(nrows = 2, sharex = True)

fr = open('./Fermi/naive_atomic.txt',"r")

x = []
y = []

for line in fr.readlines():
	arr = line.strip().split()
	x.append(eval(arr[0]))
	y.append(eval(arr[1]))

ax0.plot(x,y,'o-',label='naive')

fr.close()

fr = open('./Fermi/gather.txt',"r")

x = []
y = []

for line in fr.readlines():
	arr = line.strip().split()
	x.append(eval(arr[0]))
	y.append(eval(arr[1]))

ax0.plot(x,y,'x-',label='gather')

fr.close()

fr = open('./Kepler/naive_atomic.txt',"r")

x = []
y = []

for line in fr.readlines():
	arr = line.strip().split()
	x.append(eval(arr[0]))
	y.append(eval(arr[1]))

ax1.plot(x,y,'o-',label='naive')

fr.close()

fr = open('./Kepler/gather.txt',"r")

x = []
y = []

for line in fr.readlines():
	arr = line.strip().split()
	x.append(eval(arr[0]))
	y.append(eval(arr[1]))

ax1.plot(x,y,'x-',label='gather')

fr.close()

fig.autofmt_xdate()
ax0.set_title("Fermi", fontsize = 15)
ax1.set_title("Kepler", fontsize = 15)
plt.xlabel("number of particles", fontsize = 15)
ax0.set_ylabel("timepass (ms)", fontsize = 15)
ax1.set_ylabel("timepass (ms)", fontsize = 15)
ax0.legend(loc = "upper left", fontsize = 15)
ax1.legend(loc = "upper left", fontsize = 15)
plt.show()
