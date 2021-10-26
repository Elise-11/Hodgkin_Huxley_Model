#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:39:31 2021

@author: fabre
"""

from HH_EF_KH_model import HHModel, Simulation
import numpy as np
import matplotlib as plt

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
sim.plotSimulation()
