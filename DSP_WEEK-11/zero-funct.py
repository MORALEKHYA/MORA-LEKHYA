from matplotlib import pyplot as plt
import numpy as np
from scipy.io import signal
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

h=a/b
mag_h=np.abs(h)
phase_h=np.angle(h)
plt.plot(w,mag_h)
plt.plot(w,phase_h)
plt.show()
