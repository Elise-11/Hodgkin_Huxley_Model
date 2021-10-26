#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:39:31 2021

@author: fabre
"""
#imports 
from HH_EF_KH_model import HHModel, Simulation
import numpy as np
from matplotlib import pyplot as plt
import os

# plot the results with MatPlotLib

#possibility to change the values of the model parameter 
model = HHModel()
model.gNa = 120  # typically 120
model.gK = 36  # typically 36
model.EK = -12  # typically -12
model.ENa = 115  # typically 115

# customize a stimulus waveform
target_voltage = np.zeros(20000)
target_voltage[7000:13000] = 45  # add a square pulse

# simulate the model cell using the custom waveform
sim = Simulation(model)
sim.runSimulation(membraneVoltage=target_voltage, stepMs=0.01)


plt.figure(figsize=(10, 8))
        


#membrane potential 
ax1 = plt.subplot(311)
ax1.plot(sim.times, sim.Vm - 70, color='b')
ax1.set_ylabel("Membrane Potential (mV)")
ax1.set_xlabel(" Time (ms)")
ax1.set_title("Hodgkin-Huxley Model", fontSize=15)
textstr = 'gNa=%.2f\ngK=%.2f\nENa=%.2f\nEK=%.2f\n'%(model.gNa, model.gK, model.ENa,model.EK)
ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top')

#Currents
ax2 = plt.subplot(312, sharex=ax1)
ax2.plot(sim.times, sim.INa, label='INa', color='cyan')
ax2.plot(sim.times, sim.IK, label='IK', color = 'red')
ax2.plot(sim.times, sim.ILeak, label='ILeak', color = 'pink')
ax2.set_ylabel("Current (µA/cm²)")
ax2.set_xlabel(" Time (ms)")
ax2.legend()

#gating variable states
ax3 = plt.subplot(313, sharex=ax1)
ax3.plot(sim.times, sim.h_state, label='h', color="darkcyan")
ax3.plot(sim.times, sim.m_state, label='m', color="dodgerblue")
ax3.plot(sim.times, sim.n_state, label='n', color = "red")
ax3.set_xlabel(" Time (ms)")
ax3.set_ylabel("Gating variable activation")
ax3.legend()


#plt.text(0.02, 0,textstr, fontsize=14)
plt.tight_layout()
plt.plot()

#save each created plot 
counter = 1
filename = "HHModel{}.png"
while os.path.isfile(filename.format(counter)):
    counter += 1
filename = filename.format(counter)
plt.savefig(filename)
plt.close()
