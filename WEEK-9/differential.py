import  numpy as np
from  scipy.integrate import odeint
import matplotlib.pyplot as plt
 
 def return_dydt(y,t):
 	dydt=-y*t+13
 	return dydt
 	
 y0=1
 
 t=np.linspace(0,5)
 y=odeint(returns_dydt,y0,t)
 plt.plot(t,y)
 plt.xlabel('Time')
 plt.ylabel('Y')
 plt.show()
