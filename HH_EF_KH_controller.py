#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:39:31 2021

@author: fabre
"""

from HH_EF_KH_model import HHModel, Simulation
import numpy as np
import matplotlib as plt

#Change HHmodel parameters (matrix)
model = HHModel()
model.gNa = 120  # typically 120
model.gK = 36  # typically 36
model.EK = -12  # typically -12
model.ENa = 115  # typically 115

# customize a stimulus waveform
target_voltage = 0*np.ones(20000)
target_voltage[7000:13000] = 45  # add a square pulse

# simulate the model cell using the custom waveform
sim = Simulation(model)
sim.RunSimulation(membraneVoltage=target_voltage, stepSizeMs=0.01)
plt.figure(figsize=(10, 8))

ax1 = plt.subplot(311)
ax1.plot(sim.times, sim.Vm - 70, color='b')
ax1.set_ylabel("Membrane Potential (mV)")
ax1.set_xlabel(" Time (ms)")
ax1.set_title("Hodgkin-Huxley Spiking Neuron Model", fontSize=15)


ax2 = plt.subplot(312, sharex=ax1)
ax2.plot(sim.times, sim.INa, label='INa')
ax2.plot(sim.times, sim.IK, label='IK')
ax2.plot(sim.times, sim.IKleak, label='ILeak')
ax2.set_ylabel("Current (µA/cm²)")
ax2.set_xlabel(" Time (ms)")
ax2.legend()

plt.tight_layout()
plt.show()
#saveplot
