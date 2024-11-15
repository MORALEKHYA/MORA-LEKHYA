import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
h=[0.5,1,0.5]
def discrete_convolution(x,h):
	len_x=len(x)
	len_h=len(h)
	len_y=len_x+len_h-1
	y=[0]*len_y
	for i in range(len_y):
		for j in range(len_h):
			if i-j>=0 and i-j<len_x:
				y[i]=x[i-j]*h[j]
	return y
y=discrete_convolution(x,h)
'''print("The discrete convolution of x and h is:",y)'''
plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.stem(x)
plt.title("x[n]")
plt.subplot(3,1,2)
plt.stem(h)
plt.title("h")
plt.subplot(3,1,3)
plt.stem(y)
plt.title("Convolved signal y[n]")
plt.tight_layout()
plt.show()
