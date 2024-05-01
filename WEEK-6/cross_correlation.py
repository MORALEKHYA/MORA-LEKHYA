import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

xl = int(input("Enter length of x: "))
yl = int(input("Enter length of y: "))

print("Enter elements into x:")
for i in range(xl):
    a = int(input("Enter: "))
    x.append(a)
    
print("Enter elements into y:")
for i in range(yl):
    a = int(input("Enter: "))
    y.append(a)

z = []
for k in range(yl - 1):
    s = 0
    for n in range(xl):
        if n + k < xl:
            s += x[n] * y[n + k]
    z.append(s)

plt.plot(z)
plt.xlabel('Lag')
plt.ylabel('Cross-correlation')
plt.title('Cross-correlation between x and y')
plt.show()
