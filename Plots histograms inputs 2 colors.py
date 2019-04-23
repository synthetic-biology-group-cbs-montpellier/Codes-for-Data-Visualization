#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:37:55 2018

@author: anazuniga
"""
from FlowCytometryTools import FCPlate
from FlowCytometryTools import FCMeasurement
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats



def graph_cyto(gate, wells, output_file):
    directory=r'/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate 2 input/'
    n=0
    #plt.subplots(figsize=(4,2.4))
    plt.subplots(figsize=(8,2))
    #fig.set_size_inches(1, 1) 
    plt.subplots_adjust(hspace=0.0, wspace= 0.0)
    inp=gate
    for x in wells:
        if inp[n]=='1':
            c='#00a651'
        else:
            c='#929591'
        n+=1
        datafile=directory+'/F0/export_'+x+'_Single Cells.fcs'
        sample = FCMeasurement(ID='Test Sample', datafile=datafile)
        #density = stats.gaussian_kde(sample['BL1-H'])
        logbins = np.geomspace(10, 1000000, 100)
        ax=plt.subplot(1,16,n)
        #ax=plt.subplot(1,8,n)
        ax.hist(sample['GFP-A'], bins=logbins, orientation="horizontal", color='#929591')
        plt.yscale('log')
        #ax.set_ylim(25, 750000)
        ax.set_ylim(10, 500000)
        ax.xaxis.set_ticks_position('none')
        ax.set_xticks([])
        #ax.axhline(95000, color="black", linestyle='--', dashes=(4,4),lw=1)
        ax.axhline(77, color="black", linestyle='--', dashes=(4,4),lw=1)
        #ax.axhline(155000, color="black", linestyle='--', dashes=(4,4),lw=1)
        #ax.axhline(240, color="black", linestyle='--', dashes=(4,4),lw=1)

        n+=1
        datafile=directory+'/F0/export_'+x+'_Single Cells.fcs'
        sample = FCMeasurement(ID='Test Sample', datafile=datafile)
        #density = stats.gaussian_kde(sample['BL1-H'])
        logbins = np.geomspace(10, 1000000, 100)
        ax=plt.subplot(1,16,n)
        #ax=plt.subplot(1,8,n)
        ax.hist(sample['V1-A'], bins=logbins, orientation="horizontal", color='#929591')
        plt.yscale('log')
        #ax.set_ylim(25, 750000)
        ax.set_ylim(10, 500000)
        ax.xaxis.set_ticks_position('none')
        ax.set_xticks([])
        #ax.axhline(95000, color="black", linestyle='--', dashes=(4,4),lw=1)
        ax.axhline(72, color="black", linestyle='--', dashes=(4,4),lw=1)
        #ax.axhline(155000, color="black", linestyle='--', dashes=(4,4),lw=1)
        #ax.axhline(240, color="black", linestyle='--', dashes=(4,4),lw=1)
        #ax.xticks([])
        #ax.xlabel('')
        if n!=1:
            ax.yaxis.set_ticks_position('none')
            ax.set_yticks([])
        else:
            plt.yticks(fontsize=12)
            #ax.set_ylabel("FI (A.U.)", fontsize=14)
    #plt.savefig("/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate/D0 plots/"+output_file+".svg", format="svg")
    plt.savefig("/Users/anazuniga/Documents/phyton/FlowCytometryTools/FCplate 2 input/D0 plots/"+output_file+".pdf", format="pdf")
    
graph_cyto('02',['1_054'],'B1 D2 ara-atc')    