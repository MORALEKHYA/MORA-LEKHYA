a=[1,2]
b=[3,4]
su=0
for i in range(len(a)):
	if(type(a[i])!=type("a") and type(b[i])!=type("b")):
		p=a[i]*b[i]
		su=su+p
	else:
		print("not possible")
print("The dot product is %d"%su)
