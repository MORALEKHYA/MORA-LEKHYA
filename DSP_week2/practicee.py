#downsampling a array
'''l=[]
n=int(input("Enter the no.of time intervals:"))
print("discrete data:")
for i in range(0,n):
	k=int(input())
	l.append(k)
a=int(input("Enter scaling factor:"))
def sample(l,a):
	if(a>1):
		l2=[]
		for  i in range(0,n):
			if(a*i)<n:
				l2.append(l[a*i])
	return l2
print("The resultant downsampled array:",sample(l,a))
'''
#downsampling of an audio
#from matplotlib.pyplota as plt
#from scipy.io import wavfile

'''a=int(input("Enter  a scaling factor :"))
fs,x=wavfile.read("/home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav")
def sampling(x,a):
	if(a>1):
		y=x[::a]
		wavfile.write("ds3.wav",fs,y)
sampling(x,a)'''
#DTFT of a array

'''import matplotlib.pyplot as plt
import numpy as np
def dtft(x):
	X=[]
	w=(np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)):
			s=s+x[n]*np.exp(-1j*f*n)
			X.append(s)
		return w,X
n=np.arange(0,500)
input_signal=[-1,2,3,0.4,3.5,7,3]
#n=np.arange(0,500)
w,X=dtft(input_signal)
x_mag=np.abs(X)
x_phase=np.angle(X)
plt.subplot(2,1,1)
plt.plot(x_mag)
plt.subplot(2,1,2)
plt.plot(x_phase)
plt.show()
'''
'''import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
P=[]
Z=[]
p=int(input("Enter no.of poles"))
z=int(input("Enter no.of zeros"))
print("ENTER POLES")
for i in range(p):
	real_part=float(input("ENter real part:"))
	img_part=float(input("ENter imag_part:"))
	P.append(complex(real_part,img_part))
print("ENTER ZEROS ")
for j in range(z):
	real_part=float(input("ENter real part:"))
	img_part=float(input("Enter img_part:"))
	Z.append(complex(real_part,img_part))

z1,p1=np.array(Z),np.array(P)
b,a=signal.zpk2tf(z1,p1,1)

w,h=signal.freqz(b,a)
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
x_phase=(w,np.angle(h))
#plt.figure(figsize=(10,6))
#plt.subplot(2,1,1)
plt.plot(w,np.abs(h))

	

plt.subplot(2,1,2)
plt.plot(w,np.angle(h))
plt.tight_layout()
plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
print("ENTER ZERO PARAMETERS:")
print("ENter real part:")
r=float(input("Enter real part:"))
w_phase=float(input("Enter imag part:"))
z=np.exp(-1j*f)
def con_Ztow():
	h=[]
	for f in w:
		h.append(1-(z*np.exp(-j*f))
	return h
h=con_Ztow()




	



































		
