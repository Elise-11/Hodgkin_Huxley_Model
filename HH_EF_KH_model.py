#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:23:37 2021

@author: fabre
"""

"""
The HHModel tracks conductances of 3 channels, depending on time and voltage,
while keeping Vm at a fixed value.

The 3 channels are :
    - Potassium channel
    - Sodium channel
    - leak channel
    
NA = sodium
K = potassium
L = Leak (leakage current ions)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import warnings

class Gate:
    """The Gate object manages a channel's kinetics and open state 
    the state will be called f 
    the gating variable follows the following differential equation : ...
    the channel opens with a probability of : 
    the channel closes with a probability of : """
    alpha = 0
    beta = 0
    f = 0

    #update gating variable 
    def update(self, time):
        alphaState = self.alpha * (1-self.f)
        betaState = self.beta * self.f
        self.f += time * (alphaState - betaState)
    
    #
    def setInfiniteState(self):
        self.f = self.alpha / (self.alpha + self.beta)



class HHModel (Gate) : 
    
    #variable values from the article 
    Cm = 1
    ENa = 115
    EK = -12
    EKleak = 10.6
    gNa = 120
    gK = 36
    gKleak = 0.3
    
    #gating variable for potassium and calcium channels
    m, n, h = Gate(), Gate(), Gate()
    
    def __init__(self, startingVoltage=0):
        #initial state
        self.Vm = startingVoltage
        self.UpdateTime(startingVoltage)
        self.m.setInfiniteState()
        self.n.setInfiniteState()
        self.n.setInfiniteState()

    def UpdateTime(self, Vm):
        """Update of the time constants for the gates according to a given 
        Vm (membrane voltage)"""
        #equations fro the original article 
        self.n.alpha= 0.01 * ((10-Vm) / (np.exp((10-Vm)/10)-1))
        self.n.beta = 0.125*np.exp(-Vm/80)
        self.m.alpha = 0.1*((25-Vm) / (np.exp((25-Vm)/10)-1))
        self.m.beta = 4*np.exp(-Vm/18)
        self.h.alpha = 0.07*np.exp(-Vm/20)
        self.h.beta = 1/(np.exp((30-Vm)/10)+1)

    def UpdtateCurrents(self, membraneVoltage, time):
        """calculate currents for each channel using the latest gate time constants """
        self.INa = np.power(self.m.f, 3) * self.gNa * self.h.f*(self.Vm-self.ENa)
        self.IK = np.power(self.n.f, 4) * self.gK * (self.Vm-self.EK)
        self.IKleak = self.gKleak * (self.Vm-self.EKleak)
        self.Vm = membraneVoltage

    def UpdateGateStates(self, time):
        """calculate the new opening states of the channels according to the Vm"""
        self.n.update(time)
        self.m.update(time)
        self.h.update(time)

    def iterate(self, membraneVoltage, time):
        #function to run the 3 updates
        self.UpdateTime(self.Vm)
        self.UpdtateCurrents(membraneVoltage, time)
        self.UpdateGateStates(time)
        

    
class Simulation : 

    def __init__(self, model):
        self.model = model
        self.CreateArrays(0, 0)
        pass

    def CreateArrays(self, pointCount, time):
        self.times = np.arange(pointCount) * time
        self.Vm = np.empty(pointCount)
        self.INa = np.empty(pointCount)
        self.IK = np.empty(pointCount)
        self.IKleak = np.empty(pointCount)
        self.StateN = np.empty(pointCount)
        self.StateM = np.empty(pointCount)
        self.StateH = np.empty(pointCount)

    def RunSimulation(self, membraneVoltage, stepSizeMs):
        self.CreateArrays(len(membraneVoltage), stepSizeMs)
        print(f"simulating {len(membraneVoltage)} time points...")
        for i in range(len(membraneVoltage)):
            self.model.iterate(membraneVoltage[i], stepSizeMs)
            self.Vm[i] = self.model.Vm
            self.INa[i] = self.model.INa
            self.IK[i] = self.model.IK
            self.IKleak[i] = self.model.IKleak
            self.StateH[i] = self.model.h.f
            self.StateM[i] = self.model.m.f
            self.StateN[i] = self.model.n.f
        print("simulation complete")
        # plot the results with MatPlotLib
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



# Run a simulation

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



target_voltage2 = np.zeros(5000)
target_voltage2[1200:3800] = 20

sim2 = Simulation(model)
sim2.RunSimulation(membraneVoltage=target_voltage2, stepSizeMs=0.05)






    