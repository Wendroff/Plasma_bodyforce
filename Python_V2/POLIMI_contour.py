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

T=3.0;D=0.04;Af=2;Ny=500;Nx=1000
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
Fz = Pfd.Polimi_force(y,0.0,T,D,Af).reshape(Ny,1)*np.ones((1,Nx))
(fig_mpl,ax) = plt.subplots(1, facecolor='white',figsize=(20,7))

xx, yy = np.meshgrid(x,y)
#ax.contourf(xx,yy,Fz)

#fig_mpl.colorbar(pcm,  extend='max')
#levels = np.linspace(-7,7,15)
#pcm = ax.contourf(xx,yy,Fz,levels)
pcm = ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)
ax.set_xlabel(r'$z$',**font_label)
ax.set_ylabel(r'$y$',**font_label)
ax.set_title("POLIMI's force distribution",**font_label)
plt.yticks(**font_ticks)
plt.xticks(**font_ticks)
cbar = fig_mpl.colorbar(pcm,  extend='max')
cbar.set_label(r'$F_z$',rotation = 0,**font_label)
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_family("Times New Roman")
    l.set_size(20)
#ax.set_aspect(1)
#%%
def make_frame(t):
    #ax.clear()
    #ax.axis('off')
    #ax.set_title("POLIMI's force distribution",**font_label)

    
    # the varying weights make the points appear one after the other
    
    
    Fz = Pfd.Polimi_force(y,t,T,D,Af).reshape(Ny,1)*np.ones((1,Nx))
    
    #ax.contourf(xx, yy, Z, cmap=plt.cm.bone, alpha=0.8,
                #vmin=-2.5, vmax=2.5, levels=np.linspace(-2,2,20))
    ax.pcolor(xx,yy,Fz,vmin=-2., vmax=2.)

    return mplfig_to_npimage(fig_mpl)

animation = VideoClip(make_frame, duration = T)
animation.write_gif("POLIMI_contour.gif", fps=20)
