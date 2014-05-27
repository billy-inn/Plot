#use matplotlib to plot a decision tree
#just call the function createPlot(inTree) can complete the task
#input: a tree stored in a dictionary
#       the tree can be created recursively in this form: inTree = {rootname:{...}}
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")  #decision node style
leafNode = dict(boxstyle="round4",fc="0.8")        #leaf node style
arrow_args = dict(arrowstyle="<-")                 #array style

#plot related text
def plotMidText(cntrPt,parentPt,txtString):
	xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
	yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
	createPlot.ax1.text(xMid,yMid,txtString)

#plot related node
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',\
	xytext=centerPt,textcoords='axes fraction',\
	va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)

#the main process:plot the decision tree
def plotTree(myTree,parentPt,nodeTxt):
	numLeafs = getNumLeafs(myTree)
	depth = getTreeDepth(myTree)
	firstStr = myTree.keys()[0]
	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)
	plotMidText(cntrPt,parentPt,nodeTxt)
	plotNode(firstStr,cntrPt,parentPt,decisionNode)
	secondDict = myTree[firstStr]
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			plotTree(secondDict[key],cntrPt,str(key))
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
			plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

#totalW,totalD,xOff,yOff are all global variants
#totalW represents the total width
#totalD represents the total Depth
#xOff represents the current node's x-coordinate offset
#yOff represents the current node's y-coordinate offset
def createPlot(inTree):
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	axprops = dict(xticks=[],yticks=[])
	createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW
	plotTree.yOff = 1.0
	plotTree(inTree,(0.5,1.0),'')
	plt.show()

#get the number of leafs of myTree recursively
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			numLeafs += getNumLeafs(secondDict[key])
		else: numLeafs += 1
	return numLeafs

#get the depth of myTree recursively
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else: thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth
