import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f1=2
f2=3
x1=np.sin(2*np.pi*f1*t)
y1=np.sin(2*np.pi*f2*t)
z=x1+y1
plt.plot(t,z)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Addition of waves")
plt.show() 
