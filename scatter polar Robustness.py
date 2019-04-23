#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:57:29 2019

@author: anazuniga
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#data=pd.read_csv('/Users/anazuniga/Documents/phyton/matplot.pyplot/phyton R cells.csv',sep=",",usecols=[0,1,2],names=['program','angle','diff'])
data=pd.read_csv('/Users/anazuniga/Documents/phyton/matplot.pyplot/Robustness/All/Multicell mean.csv',sep=",",usecols=[0,1,2,3,4],names=['program','angle', 'fold', 'log', 'color'])

# Fixing random state for reproducibility
#np.random.seed(1)

# Compute areas and colors
#N = (9)
#r = (0,100)

#radius 
#radius_min = 0
#radius_max = 100
#theta = 2 * np.pi * np.random.rand(N)

theta = list(data['angle'])

# conversion of angles between degree to radiant
radiant_angle=[]
for angle in theta:
    rad=angle*np.pi/180
    radiant_angle.append(rad)
    

r = list(data['log'])

#area = 100

# definition of the colors, here the colors are dependent on the theta
color=list(data['color'])

fig = plt.figure()
ax = fig.add_subplot(111, polar=True, rscale='log')
#c = ax.scatter(theta, r, c=color, cmap='hsv', alpha=0.75)

"alternative with the dot in black"
c = ax.scatter(radiant_angle, r, c= color, cmap='winter', alpha=0.75)

#c = ax.scatter(r, theta)

#fig, ax = generate_polar_axes()
#r = np.arange(0.1, 10.0, 50.0 / len(theta))
ax.set_thetamin(0)
ax.set_thetamax(90)
ax.set_rmin(0)
ax.set_rmax(1.3)
#ax.set_rlim((0.1 , 50.0))
ax.tick_params(axis='y', pad=20)
#ax.set_rscale('log')
#ax.contourf(theta, r, r)
#ax.set_ylim((0.0, 0.5))
#ax.tick_params(labelbottom=False, labelleft=False)
#ax.set_thetalabel(lalala)
# to get the axes in the same orientation than weinberg and al.
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2 )

#plt.show()
#plt.savefig('/Users/anazuniga/Documents/phyton/matplot.pyplot/Robustness/cells.pdf')
plt.savefig('/Users/anazuniga/Documents/phyton/matplot.pyplot/Robustness/All/Multicel mean.pdf')
print plt