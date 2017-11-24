# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:43:20 2017

@author: Wendroff
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:12:08 2017

@author: Wendroff
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import Maden2013_plasma as M13

mpl.rcParams['mathtext.fontset'] = 'stix' #数学公式配合Times字体

T=3.0;Ny=500;Nx=1000
a0 = 2.0
a1 = 0.8
a2 = 1.0
b0 = 23.5
b1 = 0.7
b2 = 0.2
c  = 1.0
x0 = np.pi
y0 = 0.0
duration = T
y  = np.linspace(0,0.3,Ny)
x  = np.linspace(0,2*np.pi,Nx)

font_label = {
             'fontname':"Times New Roman",
             'size'    : 20
            }
font_ticks = {
             'fontname':"Times New Roman",
             'size'    : 12
            }

(fig_mpl,ax) = plt.subplots(1, facecolor='white')

xx, yy = np.meshgrid(x,y)
Fz = np.zeros(xx.shape)
#Max_Fz = np.abs(M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c).max())
#levels = np.linspace(-Max_Fz,Max_Fz,21)
levels = np.linspace(-5e-5,5e-5,21)
pcm = ax.contourf(xx,yy,Fz,levels)
#pcm = ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)
fig_mpl.colorbar(pcm,  extend='max')
#ax.set_aspect(1)

def make_frame(t):
    ax.clear()
    #ax.axis('off')
    ax.set_title("THU's force distribution",**font_label)

    c_t = c*np.sin(2*np.pi*t/T)
    if (c_t>0):
        Fz = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c_t)
    else:
        Fz = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c_t,False)
    
    ax.contourf(xx, yy, Fz,levels)
    #ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)

    return mplfig_to_npimage(fig_mpl)

animation = VideoClip(make_frame, duration = T)
animation.write_gif("THU_contour.gif", fps=20)
