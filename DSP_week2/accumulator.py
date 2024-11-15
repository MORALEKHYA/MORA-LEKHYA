'''import numpy as np
from matplotlib import pyplot as plt
input_signal=[1,2,3,4]
output_signal=[]
accumulator=0
N=len(input_signal)
for k in range(N):
	accumulator+=input_signal[k]
	output_signal.append(accumulator)
print(output_signal)
plt.subplot(2,1,1)
plt.stem(input_signal)
plt.subplot(2,1,2)
plt.stem(output_signal)
plt.show()
'''


#accumulator
'''import numpy as np
import matplotlib.pyplot as plt
x=[2,3,5,6]
y=[]
accumulator=0
N=len(x)
for k in range(len(x)):
	accumulator=accumulator+x[k]
	y.append(accumulator)
print("The sum of values be:")
print(y)'''


#sampling

import numpy as np
import matplotlib.pyplot as np
x=[1,87,3,4,5,6]
def sample(x,a):
	if a>1:
		y=[]
		for i in range(len(x)):
			if a*i<len(x):
				y.append(x[a*i])
	return y
y=sample(x,3)
print(y)




































