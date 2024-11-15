import numpy as np
def cyclic_delay(x,m):
	N=len(x);y=[]
	for n in range(0,N):
		if n-m>=0:
			idx=(n-m)%N
		else:
			idx=N+n-m
		y.append(x[idx])
	return y
def circ_conv(x1,x2):
	z=[]
	a=x2[1:]#excluding first elemnt
	x2r=np.concatenate(([x2[0]],a[::-1]))#keeping first element as it is and reversing remaining elements
	
	for n in range(len(x1)):
		y=cyclic_delay(x2r,n)
		z.append(np.dot(x1,y))
	return z
x1=[1,2,3,4]
x2=[-1,0,5,3]
print(circ_conv(x1,x2))
