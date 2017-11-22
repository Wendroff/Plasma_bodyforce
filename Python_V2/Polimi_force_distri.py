# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:22:42 2017

@author: lthpc
"""

import numpy as np

def Polimi_force(y=np.linspace(0,1,500),t=0,T=1.0,D=0.04,Af=2):
    #y  = np.linspace(0,1,Ny)
    Fz = Af*np.exp(-y/D)*np.cos(2*np.pi*t/T)
    return Fz