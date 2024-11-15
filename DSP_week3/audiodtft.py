import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
def dtft(x):
	X=[]
	w=np.arange(-np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)):
			s=s+x[n]*np.exp(-1j*f*n)
		X.append(s)
	return w,X
n=np.arange(0,500)
fs,X=wavfile.read('/home/rguktrkvalley/Pictures/DSP Lab/week2/npy.wav')
if len(X.shape) > 1:
    X= X.mean(axis=1)
#X = X.astype(float)
w,X=dtft(X)
x_magnitude=np.abs(X)
x_angle=np.angle(X)
plt.subplot(2,1,1)
plt.plot(w,x_magnitude)
plt.subplot(2,1,2)
plt.plot(w,x_angle)
plt.show()
