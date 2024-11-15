import numpy as np
from matplotlib import pyplot as plt
def dtft(x):
	X_dtft=[]
	w=np.arange(-np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)):
			s=s+x[n]*np.exp(-1j*f*n)
		X_dtft.append(s)
	return w,X_dtft
n=np.arange(0,500)
input_signal=[-1,2,3,0.4,3.5,7,3]
w,X_dtft=dtft(input_signal)
x_magnitude=np.abs(X_dtft)
x_angle=np.angle(X_dtft)
plt.subplot(2,1,1)
plt.plot(w,x_magnitude)
plt.subplot(2,1,2)
plt.plot(w,x_angle)
plt.show()
