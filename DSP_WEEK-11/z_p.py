from matplotlib import pyplot as plt
import numpy as np
n=int(input("Enter no.of zeros"))
z=[]
p=[]
for i in range (0,n):
	r=float(input("zero location from origin"))
	wo=int(input("Enter freq of zeros"))
	z.append(r*np.exp(1j*wo))
for i in range(0,n):
	r=float(input("ploes location from origin"))
	wo=int(input("Enter freq of poles"))
	p.append(r*np.exp(1j*wo))
w=np.arange(-np.pi,np.pi,0.0001*np.pi)
a=1
b=1
for i in range (0,len(z)):
	a=1-(z[i]*np.exp(1j*w))*a
for i in range (0,len(p)):
	b=1-(z[i]*np.exp(1j*w))*b

h=a/b
mag_h=np.abs(h)
phase_h=np.angle(h)
plt.plot(w,mag_h)
plt.plot(w,phase_h)
plt.show()
