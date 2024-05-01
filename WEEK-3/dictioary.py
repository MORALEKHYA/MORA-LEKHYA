import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sindict={'s1':[2,5],'s2':[5,10],'s3':[3,7],'s4':[10,12],'s5':[1,2]}
k=input("Enter sinosodial key to generate ")
if sindict[k]:
	x=sindict[k][0]*np.sin(2*np.pi*sindict[k][1]*t)
	plt.plot(t,x)
	plt.show()
