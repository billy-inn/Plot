import plotDim as p1
import plotPorder as p2
import plotPhi as p3

for i in ["naive","gather","matrix"]:
	for j in ["4","6"]:
		for k in ["0.1","0.2","0.3","0.4","0.5"]:
			p1.plot(i,j,k)
	
	for j in ["32","64","128"]:
		for k in ["0.1","0.2","0.3","0.4","0.5"]:
			p2.plot(i,j,k)

	for j in ["32","64","128"]:
		for k in ["4","6"]:
			p3.plot(i,j,k)

