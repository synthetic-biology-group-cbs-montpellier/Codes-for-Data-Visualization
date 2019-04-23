#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:12:54 2019

@author: anazuniga
"""

"""
Created on Tue Nov 20 19:16:32 2018

@author: anazuniga
"""


import os

from pylab import *

import FlowCytometryTools
from FlowCytometryTools import FCMeasurement



#datafile = os.path.join(datadir, 'export_G5_Single Cells.fcs')

#datafile = r'/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate 2 input/B2/export_G5_Single Cells.fcs' 
#fig, axs = plt.subplots(3, 1)
#figure();
# Initialize a Figure 
fig = plt.figure()


# Add Axes to the Figure
#fig.add_axes([0,0,1,1])
#fig, axs = plt.subplots(3, 1)
#fig.subplots_adjust(hspace=0.0, wspace= 0.0)
plt.subplots(figsize=(2,2))
subplots_adjust(hspace=0.0, wspace= 0.0)
# Load data
datafile = r'/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate 2 input/2MP1/export_P7R_Single Cells.fcs' 
tsample = FCMeasurement(ID='Test Sample', datafile=datafile)
tsample = tsample.transform('hlog', channels=['GFP-H', 'SSC-H', 'mCherry-H', 'FSC-H', 'V1-H'], b=200.0)
ax = subplot(3,1,1)
# Plot
#tsample.plot(['YL2-H', 'SSC-H'], bins=100, alpha=2, cmap=cm.hot);
tsample.plot(['V1-H', 'SSC-H'], kind='scatter', alpha=0.05, color='black', s=1);
ax.tick_params(labelbottom=False, labelleft=False)
#ax1.set_ylim(0, 10000)
#plt.scale('log')
#logbins = np.geomspace(10, 1000000, 100)
#plt.xscale('log')
#ax1.set_yscale('log')
ax.set_ylim(1000, 10000)
#ax1.set_xlim(0, 10000)
#ax1.xaxis.set_label_position('none')
#ax.set_yticks('')
ax.set_ylabel('')
ax.set_xlabel('')
grid(False)

ax1 = subplot(3,1,2, sharey=ax, sharex=ax)
#tsample.plot(['BL1-H', 'SSC-H'], bins=100, alpha=0.9, cmap=cm.hot);
tsample.plot(['mCherry-H', 'SSC-H'], kind='scatter', alpha=0.05, color='black', s=1);
#plt.yscale('log')
ax1.tick_params(labelbottom=False, labelleft=False)
ax1.set_ylabel('')
ax1.set_xlabel('')
#ax2.set_label([])
ax1.set_ylim(1000, 10000)
#ax2.set_xlim(0, 10000)
#plt.delaxes('ax2')
#ax2.legend('none')

ax2 = subplot(3,1,3, sharey=ax1, sharex=ax1)
#tsample.plot(['BL1-H', 'SSC-H'], bins=100, alpha=0.9, cmap=cm.hot);
tsample.plot(['GFP-H', 'SSC-H'], kind='scatter', alpha=0.05, color='black', s=1);
#plt.yscale('log')
ax2.tick_params(labelbottom=False, labelleft=False)
ax2.set_ylabel('')
ax2.set_xlabel('')
#ax2.set_label([])
ax2.set_ylim(1000, 10000)
#ax3.set_xlim(0, 10000)
#plt.delaxes('ax2')
#ax2.legend('none')
grid(False)


# show() # <-- Uncomment when running as a script
plt.savefig('/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate 2 input/D0 plots/2MP1 atc-ara.pdf')
#plt.plot(x, y, 'r-', rasterized=True)
print plt
