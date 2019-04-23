# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd



data=pd.read_csv('/Users/anazuniga/Documents/phyton/matplot.pyplot/2iM2.csv',sep=",",usecols=[0,1,2,3,4,5,6,7,8],names=['input','strain_name','mean_fluoGFP','error_meanGFP', 'mean_fluoRFP','error_meanRFP', 'mean_fluoBFP','error_meanBFP', 'color'])
 
#def set_size_inches(self, w, h=None, forward=True):
#fig.set_size_inches(1, 1) 
#plt.subplots(figsize=(2,1))
fig, axs = plt.subplots(1, 1)
fig.subplots_adjust(hspace=0.0, wspace= 0.0)
#plt.subplots_adjust(hspace=0.0, wspace= 0.5)
fig.set_size_inches(1, 1) 

ax1=plt.subplot(133)


number_of_points=0
bar_width=1
ax1.bar(range(0,1), data['mean_fluoGFP'][4], bar_width, yerr=data['error_meanGFP'][4], align='center', color=data['color'][0], alpha=1, error_kw=dict(ecolor='k', lw=1, capsize=3, capthick=1))
#ax1.set_xlim(left=-0.7, right=number_of_points-0.3)
ax1.set_ylim(bottom=0, top=15000)
ax1.tick_params(labelbottom=False, labelleft=False)
#ax1.ticklabel_format(style='sci',scilimits=(0,0),axis='both')
#ax1.axis.set_yticks_position (labelrigth= True) 
#ax1.set_ylabel("G", fontsize=8)
ax1.set_yticks(range(0))
ax1.set_yscale("linear", nonposy='clip')
#ax1.yaxis.set_ticks_position('none')
#ax1.set_xticklabels(data['input'][1], fontsize=8, rotation='vertical')
ax1.xaxis.set_ticks_position('none')
ax1.set_yticks([0])
#ax1.set_xlabel("G", fontsize=8)
#ax.set_ylabel("GFP/abs600", fontsize=8)
#ax1.tick_params(axis='y', which='major', labelsize=8)
ax1.axhline(1358, color="black", linestyle='--', dashes=(1,1),lw=2)
#ax.axhline(1, color="black", linestyle='--', dashes=(10,10),lw=1)


ax=plt.subplot(132)


number_of_points=0
bar_width=2
ax.bar(range(0,1), data['mean_fluoRFP'][4], bar_width, yerr=data['error_meanRFP'][4], align='center', color=data['color'][1], alpha=1, error_kw=dict(ecolor='k', lw=1, capsize=3, capthick=1))
#ax.set_xlim(left=-0.7, right=number_of_points-0.3)
ax.set_ylim(bottom=0, top=1300)
ax.tick_params(labelbottom=False, labelleft=False)
ax.set_yticks(range(0))
ax.set_yscale("linear", nonposy='clip')
#ax.set_xticklabels(data['input'][0:1], fontsize=8, rotation='vertical')
ax.xaxis.set_ticks_position('none')
ax.set_yticks([0])
#ax.set_xlabel("R", fontsize=8)
#ax.set_ylabel("RFP/abs600", fontsize=8)
ax.tick_params(axis='y', which='major', labelsize=8)
ax.axhline(79, color="black", linestyle='--', dashes=(1,1),lw=2)
#ax.axhline(1, color="black", linestyle='--', dashes=(10,10),lw=1)


#ax=plt.subplot(131)


#number_of_points=0
#bar_width=2
#ax.bar(range(0,1), data['mean_fluoBFP'][15], bar_width, yerr=data['error_meanBFP'][15], align='center', color=data['color'][2], alpha=1, error_kw=dict(ecolor='k', lw=1, capsize=3, capthick=1))
#ax.set_xlim(left=-0.7, right=number_of_points-0.3)
#ax.set_ylim(bottom=0, top=9000)
#ax.tick_params(labelbottom=False, labelleft=False)
#ax.set_yticks(range(0))
#ax.set_yscale("linear", nonposy='clip')
#ax.set_xticklabels(data['input'][0:1], fontsize=8, rotation='vertical')
#ax.xaxis.set_ticks_position('none')
#ax.set_yticks([0])
#ax.set_xlabel("B", fontsize=8)
#ax.set_ylabel("BFP/abs600", fontsize=8)
#ax.tick_params(axis='y', which='major', labelsize=8)
#ax.axhline(1100, color="black", linestyle='--', dashes=(1,1),lw=2)
#ax.axhline(1, color="black", linestyle='--', dashes=(10,10),lw=1)

plt.savefig('/Users/anazuniga/Documents/phyton/matplot.pyplot/graph 2input multicell/Ara-atc 2MP2.pdf')

print plt