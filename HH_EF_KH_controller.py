#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabre
"""
#imports 
from HH_EF_KH_model import HHModel, Simulation
import numpy as np
from matplotlib import pyplot as plt
import os
import tkinter as tk

# plot the results with MatPlotLib
model = HHModel()


def setParam(Cm, gNa, gK, gLeak,ENa, EK,ELeak):
    #possibility to change the values of the model parameter 
    model.Cm = Cm#typically 1 
    model.gNa = gNa # typically 120
    model.gK = gK # typically 36
    model.gLeak = gLeak #typicaly 0.03
    model.ENa = ENa  # typically 115
    model.EK = EK  # typically -12
    model.ELeak = ELeak #typically 10.6
    return(Cm, gNa, gK, gLeak,ENa, EK,ELeak)

#essayer de mettre param direct dans plotSimulation
def plotSimulation(): 
    # customize a stimulus waveform
    stimu = np.zeros(20000)
    stimu[7000:13000] = 45  # add a square pulse
    
    # simulate the model cell using the custom waveform
    sim = Simulation(model)
    sim.runSimulation(membraneVoltage=stimu, stepMs=0.01)
    
    Fig1 = plt.figure(figsize=(8, 6))
    
    #stimulation
    ax1 = Fig1.add_subplot(411)
    ax1.plot(sim.times, stimu, color='deeppink')
    ax1.set_ylabel("Stimulation (µA/cm²)",fontsize = 8)
    ax1.set_xlabel(" Time (ms)")
    ax1.set_title("Hodgkin-Huxley Model", fontsize=15)
    textstr = 'Cm=%2f\ngNa=%.2f\ngK=%.2f\ngLeak=%2f\nENa=%.2f\nEK=%.2f\nELeak=%.2f\n'%(model.Cm,model.gNa, model.gK, model.gLeak, model.ENa,model.EK,model.ELeak)
    ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes,
            verticalalignment='top')
    
    
    #gating variable states
    ax2 = Fig1.add_subplot(412, sharex=ax1)
    ax2.plot(sim.times, sim.h_state, label='h', color="darkcyan")
    ax2.plot(sim.times, sim.m_state, label='m', color="dodgerblue")
    ax2.plot(sim.times, sim.n_state, label='n', color = "red")
    ax2.set_xlabel(" Time (ms)")
    ax2.set_ylabel("Gating variable activation", fontsize = 8)
    ax2.legend(loc="upper right")
    
    #Currents
    ax3 = Fig1.add_subplot(413, sharex=ax1)
    ax3.plot(sim.times, sim.INa, label='INa', color='cyan')
    ax3.plot(sim.times, sim.IK, label='IK', color = 'red')
    ax3.plot(sim.times, sim.ILeak, label='ILeak', color = 'pink')
    ax3.set_ylabel("Current (µA/cm²)",fontsize = 8)
    ax3.set_xlabel(" Time (ms)")
    ax3.legend(loc = "upper right")
    
    #membrane potential 
    ax4 = Fig1.add_subplot(414)
    ax4.plot(sim.times, sim.Vm-70, color='b')
    ax4.set_ylabel("Potential (mV)",fontsize = 8)
    ax4.set_xlabel(" Time (ms)")

    #plt.text(0.02, 0,textstr, fontsize=14)
    Fig1.tight_layout()
    return Fig1



def savePlot():
    #save each created plot 
    Figure = plotSimulation()
    filename = "HHModel{}.png"
    counter = 0
    while os.path.isfile(filename.format(counter)):
        counter += 1
    filename = filename.format(counter)
    Figure.savefig(filename)


#setParam(14,120,36,0.03,115,-12,10.6)
#plotSimulation()
#savePlot()


