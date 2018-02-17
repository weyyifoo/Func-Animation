# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:15:36 2018

@author: Wey Yi
"""

# Func Animation tutorial

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# panel setup for where the function will be plotted unto
fig1 = plt.figure()
ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
line, = ax.plot([], [], lw = 2)

# initialization function: plotting the background of each frame
def init():
    line.set_data([], [])
    return line,

# define function and animate
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animation.
anim = animation.FuncAnimation(fig1, animate, init_func = init, 
                               frames = 200, interval = 20,
                               blit = True)

plt.show()