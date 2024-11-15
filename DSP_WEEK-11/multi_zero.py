from matplotlib import pyplot as plt
import numpy as np
n=int(input("Enter no.of zeros"))
z=[]
for i in range (0,n):
	r=float(input("zero location from origin"))
	wo=int(input("Enter freq of zeros"))
	z.append(r*np.exp(1j*wo))
w=np.arange(-np.pi,np.pi,0.0001*np.pi)
p=1
for i in range (0,len(z)):
	p=1-(z[i]*np.exp(1j*w))*p
h=p
mag_h=np.abs(h)
phase_h=np.angle(h)
plt.plot(w,mag_h)
plt.plot(w,phase_h)
plt.show()
