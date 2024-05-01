import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=9
x=np.sin(2*np.pi*f*t)
with open("file.txt","w") as k:
	 k.write(str(x))
