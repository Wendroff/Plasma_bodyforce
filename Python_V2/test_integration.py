# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:06:18 2017

@author: Wendroff
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a1 = 1;
a2 = 1;
a0 = 1

def X_f(x,a0,a1,a2):
    Xf = (a2*np.power(x,2) + a1*x)*np.exp(-a0*x)
    return Xf

def Y_f(x,a0,a1,a2):
    Xf = (a2*np.power(x,2) + a1*x)*np.exp(-a0*np.power(x,0.4))
    return Xf

x = np.linspace(0,20,200)
y = X_f(x,a0,a1,a2)

#plt.plot(x,y)

answer1 = simps(y,x)
answer2 = (a0*a1+2.0*a2)/(a0**3)

print("Numerical  solution",answer1)
print("Analytical solution",answer2)

x = np.linspace(0,2000,400)
y = Y_f(x,a0,a1,a2)

plt.plot(x,y)

answer1 = simps(y,x)
answer2 = 60.0*a1/(a0**5.0)+4678.135764*a2/(a0**7.5)

print("Numerical  solution",answer1)
print("Analytical solution",answer2)

