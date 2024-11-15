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
	return X
n=np.arange(0,500)
x1=np.array([1,2,3,4])
x2=np.array([3,4,5,6])
X1=dtft(x1)
X2=dtft(x2)
X3=x1+x2
X3=dtft(X3)
k=X1+X2
x_mag=np.abs(k)
x3_mag=np.abs(X3)
plt.subplot(2,1,1)
plt.plot(x_mag)
plt.subplot(2,1,2)
plt.plot(x3_mag)
plt.show()
'''if(X1+X2==X3):
	print("linearity property is verified")
else:
	print("linearity property is not verified")'''
