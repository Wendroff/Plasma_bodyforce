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
a0 = 6.0
a1 = 2.5
a2 = 9.0
b0 = 20
b1 = 0.7
b2 = 0.1
c  = 83041.1435082426
x0 = -np.pi/3.0
y0 = 0.0
duration = T
y  = np.linspace(0,0.2,Ny)
x  = np.linspace(0,2*np.pi,Nx)

font_label = {
             'fontname':"Times New Roman",
             'size'    : 30
            }
font_ticks = {
             'fontname':"Times New Roman",
             'size'    : 20
            }

(fig_mpl,ax) = plt.subplots(1, facecolor='white',figsize=(20,7))

xx, yy = np.meshgrid(x,y)

Fz_pos     = np.zeros(xx.shape)
Fz_neg     = np.zeros(xx.shape)
Fz,f_total = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,True)
Fz_pos += Fz


x0     += (2.0*np.pi/3.0)
Fz,_       = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,True)
Fz_pos += Fz
Fz,_       = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,False)
Fz_neg += Fz

x0     += (2.0*np.pi/3.0)
Fz,_       = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,True)
Fz_pos += Fz
Fz,_      = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,False)
Fz_neg += Fz

x0     += (2.0*np.pi/3.0)
Fz,_       = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,True)
Fz_pos += Fz
Fz,_      = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,False)
Fz_neg += Fz

x0     += (2.0*np.pi/3.0)
Fz,_       = M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c,False)
Fz_neg += Fz
Fz     = np.zeros(xx.shape)
#Max_Fz = np.abs(M13.Plasma_model(xx, yy,x0,y0,a0,a1,a2,b0,b1,b2,c).max())
#levels = np.linspace(-Max_Fz,Max_Fz,21)
levels = np.linspace(-7,7,15)
pcm = ax.contourf(xx,yy,Fz,levels)
ax.set_xlabel(r'$z$',**font_label)
ax.set_ylabel(r'$y$',**font_label)
ax.set_title("THU's force distribution",**font_label)
plt.yticks(**font_ticks)
plt.xticks(**font_ticks)
#pcm = ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)
cbar = fig_mpl.colorbar(pcm,  extend='max')
cbar.set_label(r'$F_z$',rotation = 0,**font_label)
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_family("Times New Roman")
    l.set_size(20)
#cbar.ax.tick_params(labelsize=20,fontname="Times New Roman")
#ax.set_aspect(1)
#%%
def make_frame(t):
    #ax.clear()
    #ax.axis('off')
    

    c_t = np.cos(2*np.pi*t/T)
    if (c_t>0):
        Fz = c_t*Fz_pos
    else:
        Fz = c_t*Fz_neg
    
    ax.contourf(xx, yy, Fz,levels)
    #ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)

    return mplfig_to_npimage(fig_mpl)

animation = VideoClip(make_frame, duration = T)
animation.write_gif("THU_contour.gif", fps=20)
