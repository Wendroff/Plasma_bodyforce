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
import Polimi_force as Pfd

mpl.rcParams['mathtext.fontset'] = 'stix' #数学公式配合Times字体

T=1.0;D=0.04;Af=2;Ny=500;Nx=1000
duration = T
y  = np.linspace(0,0.2,Ny)
x  = np.linspace(0,2*np.pi,Nx)

font_label = {
             'fontname':"Times New Roman",
             'size'    : 20
            }
font_ticks = {
             'fontname':"Times New Roman",
             'size'    : 12
            }
Fz = Pfd.Polimi_force(y,0.0,T,D,Af).reshape(Ny,1)*np.ones((1,Nx))
(fig_mpl,ax) = plt.subplots(1, facecolor='white')

xx, yy = np.meshgrid(x,y)
#ax.contourf(xx,yy,Fz)
pcm = ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)
fig_mpl.colorbar(pcm,  extend='max')
#ax.set_aspect(1)

def make_frame(t):
    ax.clear()
    #ax.axis('off')
    ax.set_title("POLIMI's force distribution",**font_label)

    
    # the varying weights make the points appear one after the other
    
    
    Fz = Pfd.Polimi_force(y,t,T,D,Af).reshape(Ny,1)*np.ones((1,Nx))
    
    #ax.contourf(xx, yy, Z, cmap=plt.cm.bone, alpha=0.8,
                #vmin=-2.5, vmax=2.5, levels=np.linspace(-2,2,20))
    ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)

    return mplfig_to_npimage(fig_mpl)

animation = VideoClip(make_frame, duration = T)
animation.write_gif("POLIMI_contour.gif", fps=20)
