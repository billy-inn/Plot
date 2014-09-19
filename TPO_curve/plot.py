import matplotlib.pyplot as plt

def plot(filename,title):
	fig, ax = plt.subplots()
	
	fr = open(filename,'r')
	score = fr.readlines()
	fr.close()

	n = len(score)

	plt.plot(range(1,n+1),score)
	plt.title(title)
	plt.xlabel('TPO')
	plt.ylabel('Score')
	ax.set_xlim(1,n)
	ax.set_ylim(15,30)
	plt.show()
