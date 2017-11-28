# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:04:45 2017

@author: Wendroff
"""
import numpy as np
import matplotlib.pyplot as plt

def Plasma_model(x,y,x0=0.0,y0=0.0,a0 = 23.0,a1 = 0.8,a2 = 1.0,b0 = 23.5,b1 = 0.7,b2 = 0.2,c = 1.0,dirction=True):
    #x,y : the mesh in np.array form
    #a,b,c : parameters of the plasma model
    #dirction : the dirction of the body force, True for x-positive
    if (x.shape != y.shape):
        raise ValueError("The shape of array x is different with array y!")
    xx = x.copy()
    yy = y.copy()
    FX = np.zeros(xx.shape) #the spanmwise distribution which is only depends on x
    FY = np.zeros(yy.shape) #the wall-normal distribution which is only depends on y
    yy -= y0
    xx -= x0
    if (not dirction):
        xx = -xx
    flag_compute = (xx>0) & (yy>0)
    FX[flag_compute] = (a1*xx[flag_compute] + a2*np.power(xx[flag_compute],2)) * np.exp(-a0*xx[flag_compute])
    FY[flag_compute] = (b1*yy[flag_compute] + b2*np.power(yy[flag_compute],2)) * np.exp(-b0*np.power(yy[flag_compute],0.4))
    Fz = c*FX*FY
    F_total = c
    F_total *= ((a0*a1+2.0*a2)/(a0**3))
    F_total *= (60.0*b1/(b0**5.0)+4678.135764*b2/(b0**7.5))
    return Fz,F_total

if __name__ == '__main__':
    Ny=500;Nx=1000
    y  = np.linspace(0,1,Ny)
    x  = np.linspace(0,2*np.pi,Nx)
    xx, yy = np.meshgrid(x,y)
    a0 = 23.0
    a1 = 0.8
    a2 = 1.0
    b0 = 23.5
    b1 = 0.7
    b2 = 0.2
    c  = 1.0
    x0 = 0.0
    y0 = 0.0
    Fz,f_total = Plasma_model(xx,yy,x0,y0,a0,a1,a2,b0,b1,b2,c)
    
    (fig_mpl,ax) = plt.subplots(1, facecolor='white')
    #pcm = ax.pcolor(xx,yy,Fz)
    ax.contourf(xx,yy,Fz)
    
    
    
    

    