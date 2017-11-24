# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:17:12 2017

@author: Wendroff
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import Polimi_force as Pfd
mpl.rcParams['mathtext.fontset'] = 'stix' #数学公式配合Times字体
# DRAW A FIGURE WITH MATPLOTLIB
#Parameters
T=1.0;D=0.04;Af=2;Ny=500
duration = T
y  = np.linspace(0,1,Ny)
Fz = Pfd.Polimi_force(y,0.0,T,D,Af)
(fig_mpl,ax) = plt.subplots(1, facecolor='white')

font_label = {
             'fontname':"Times New Roman",
             'size'    : 20
            }
font_ticks = {
             'fontname':"Times New Roman",
             'size'    : 12
            }

#xx = np.linspace(-2,2,200) # the x vector
#zz = lambda d: np.sinc(xx**2)+np.sin(xx+d) # the (changing) z vector
ax.set_title("POLIMI's force distribution",**font_label)
ax.set_xlabel(r'$F_z$',**font_label)
#ax.set_xticklabels(ax.get_xticklabels(),**font_label)
plt.yticks(**font_ticks)
plt.xticks(**font_ticks)
plt.grid(True,linestyle = "-.")
ax.set_ylim(0.0,0.2)
ax.set_xlim(-Af,Af)
line, = ax.plot(Fz,y, lw=3)
 
# ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.


def make_frame_mpl(t):
    Fz = Pfd.Polimi_force(y,t,T,D,Af)
    line.set_xdata( Fz )  # <= Update the curve
    return mplfig_to_npimage(fig_mpl) # RGB image of the figure
 
animation =mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_gif("POLIMI.gif", fps=20)