'''

Created by vermanil
Variation of Linear Regression cost function with Theta
Hypothesis is a sigmoid Function

'''
import numpy as np
import matplotlib.pyplot as plt
x = [1, 34.6236596245, 78.0246928154]
theta = np.c_[np.linspace(-50,50,100), np.linspace(-25,25,100), np.linspace(-10,10,100)]
#print theta
# theta1 = np.linspace(-15,15,100)
# theta2 = np.linspace(-15,15,100)
z = theta[:,0] * x[0] + theta[:,1] * x[1] + theta[:,2] * x[2]
#print z
#print np.exp(1)
# plt.plot(z)
htheta = (1)/(1+np.exp(-z))
# plt.plot(htheta)
print np.square(htheta)/(2)
plt.plot(np.square(htheta)/(2))
#plt.plot(-(np.log(1-htheta)))
# plt.plot(htheta)
# x = np.linspace(-50,50,100)
# htheta = (1)/(1+np.exp(-x))
# plt.plot(htheta)
plt.show()

 