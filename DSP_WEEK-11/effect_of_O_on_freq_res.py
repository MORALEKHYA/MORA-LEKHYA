from matplotlib import pyplot as plt
import numpy as np
r=float(input("zero location from origin"))
wo=int(input("Enter freq of zeros"))
z1=r*np.exp(1j*wo)
w=np.arange(-np.pi,np.pi,0.0001*np.pi)
h=1-(z1*np.exp(1j*w))
mag_h=np.abs(h)
phase_h=np.angle(h)
plt.plot(mag_h)
plt.plot(phase_h)
plt.show()
