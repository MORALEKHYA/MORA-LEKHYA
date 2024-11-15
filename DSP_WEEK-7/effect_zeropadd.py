x=[1,2,3,4]
x1=[1,2,3,4,0,0]
x2=[1,2,3,4,0,0,0,0,0]
import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*n*k/N)
		X.append(s)
	return X
n=np.arange(1000)
N=len(x)
M=len(x1)
L=len(x2)
X=dft(x,N)
X1=dft(x1,M)
X2=dft(x2,L)
X_magnitude=np.abs(X)
plt.subplot(3,1,1)
plt.plot(X_magnitude)
X1_magnitude=np.abs(X1)
plt.subplot(3,1,2)
plt.plot(X1_magnitude)
X2_magnitude=np.abs(X2)
plt.subplot(3,1,3)
plt.plot(X2_magnitude)
plt.show()
