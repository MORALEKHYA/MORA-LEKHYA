import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
h=[0.2,0.5,0.2]
p=h[::-1]
l=len(x)
m=len(h)
N=l+m-1
y=[0]*N
for i in range(0,N):
	for j in range(m):
		y[i]=y[i]+x[i-j]*h[j]
print("The discrete convolution of x and h is:",y)
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
		
		
