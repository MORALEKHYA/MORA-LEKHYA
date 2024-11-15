import numpy as np
from matplotlib import pyplot as plt
def dtft(x):
	X=np.array([])
	w=np.arange(-np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)):
			s=s+x[n]*np.exp(-1j*f*n)
		X=np.append(X,s)
	return  w,X
n=np.arange(0,500)
x1=np.array([1,2,3,4,0,0,0])
x_delay=np.append(np.zeros(3),x1)
w1,X=dtft(x1)
w2,X2=dtft(x_delay)
X1=X*np.exp(-1j*w1*3)
x1_mag=np.abs(X1)
x2_mag=np.abs(X2)
plt.subplot(2,1,1)
plt.plot(x1_mag)
plt.subplot(2,1,2)
plt.plot(x2_mag)
plt.show()
