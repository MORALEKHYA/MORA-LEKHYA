import numpy as np
from matplotlib import pyplot as plt
x=[-1,1,2]
y=[]
a=3
for i in x:
	y.append(i)
	for j in range(0,a-1):
		y.append(0)
print(y)
plt.subplot(2,1,1)
plt.stem(x)
plt.subplot(2,1,2)
plt.stem(y)
plt.show()
