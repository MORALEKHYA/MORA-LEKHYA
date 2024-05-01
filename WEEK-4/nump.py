import numpy as np
t=np.arange(0,1,0.01)
f=9
x=np.sin(2*np.pi*f*t)
with open("nu.npy","wb") as k:
	np.save(k,x)
