l=[]
n=int(input("Enter number of samples in a time interval:"))
print("Enter discrete data:")
for i in range(0,n):
	k=int(input())
	l.append(k)
a=int(input("Enter your sacling factor:"))
def down_sample(l,a):
	if(a>1):
		l2=[]
		for i in range(0,n):
			if(a*i)<n:
				l2.append(l[a*i])
	return l2
print("After downsampling",down_sample(l,a))

