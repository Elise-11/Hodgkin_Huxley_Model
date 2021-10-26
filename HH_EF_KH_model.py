#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:23:37 2021

@author: fabre
"""

"""
The Hodgkin-Huxley model is a mathematical model describing action potentials 
of neurons. It is composed of nonlinear differential equations 
that approximate the electrical characteristics of excitable cells. 

The Hodgkin Huxley Model tracks conductances of 3 channels, 
depending on time and voltage,while keeping electrical potential of the
membrane at a fixed value.

The 3 channels are :
    - Potassium channel
    - Sodium channel
    - leak channel
    
NA = sodium
K = potassium
L = Leak (leakage current ions)
"""

import numpy as np
import matplotlib.pyplot as plt

class Gate:
    """
    The Gate class contains the functions related to the state of the open 
    or closed channels which depends on the time and is controlled by the 
    gating variable f, which follows the following differential equation: 
        df/dt = αf (1-f)- ßf(f)
    the channel opens for: 
        dα/dt = α (1-f)
    the channel closes for : 
        dß/dt = ß(f)
    """
    #initialization of variables to 0 
    alpha = 0
    beta = 0
    f = 0

    #update gating variable 
    def update(self, time):
        """
        Equations
        ----------
        f  : gating variable 
            The propotion of open channels, it depends on time and is equal to 
            (rate at wich closed channels open)-(rate at wich open channels close)
        
        alphaRate : propotion of closed channels for which the channels open
        
        betaRate : propotion of open channels for which the channels close
        """
        alphaRate = self.alpha * (1-self.f)
        betaRate = self.beta * self.f
        self.f += time * (alphaRate - betaRate)


class HHModel (Gate) : 
    """
    The HHModel class contains the differential equations of the Hodgki Huxley
    nmodel allowing to follow the currents of the ions as well as the mebrane
    potential during the time. 
    """
    #value of the different variables from the original article 
    
    #electrical capacity of the lipid membrane
    Cm = 1
    
    #electrical potential of the different channels
    ENa = 115
    EK = -12
    ELeak = 10.6
    
    #channel conductivity 
    gNa = 120
    gK = 36
    gLeak = 0.3
    
    #gating variable for potassium (n) and sodium channels (m and h)
    n, m, h = Gate(), Gate(), Gate()
    
    def __init__(self, startingVoltage=0):
        """
        Define initial state
        """
        self.Vm = startingVoltage
        self.setGatingVar(startingVoltage)


    def setGatingVar(self, Vm):
        """
        Equations
        ----------
        α and ß rate equations for each type of ion channel, depending on Vm, 
        from the original article
        
        Parameters
        ----------
        Vm : electrical potential of the membrane 

        """
        self.n.alpha= 0.01 * ((10-Vm) / (np.exp((10-Vm)/10)-1))
        self.n.beta = 0.125*np.exp(-Vm/80)
        self.m.alpha = 0.1*((25-Vm) / (np.exp((25-Vm)/10)-1))
        self.m.beta = 4*np.exp(-Vm/18)
        self.h.alpha = 0.07*np.exp(-Vm/20)
        self.h.beta = 1/(np.exp((30-Vm)/10)+1)

    def updateCurrents(self, membraneVoltage, time):
        """
        Equations
        ----------
        Current formed by the passage of each type of ion through the channels 
        the sodium channels letting in Na ions and the potassium channels and 
        the leakage channel letting out K ions depending on time and membrane 
        voltage (Vm).
        
        
        GNa = gNa * m**3 * h 
        (m**3 : three activation gate and h : one inactivation gate)
        INa = Gna(Vm - ENa)

        GK = gK * n**4 (n**4 : four activation gate )
        IK = Gk(Vm- EK)
        
        Gl = gLeak
        ILeak = Gl(Vm - ELeak)
        """
        self.Vm = membraneVoltage
        self.INa = np.power(self.m.f, 3) * self.gNa * self.h.f*(self.Vm-self.ENa)
        self.IK = np.power(self.n.f, 4) * self.gK * (self.Vm-self.EK)
        self.ILeak = self.gLeak * (self.Vm-self.ELeak)
        

    def updateGate(self, time):
        """
        updateGate allows to update gating variable for each channel
        according to the Vm and the time. 
        """
        self.n.update(time)
        self.m.update(time)
        self.h.update(time)

    def runModel(self, membraneVoltage, time):
        """
        runModel function allows to launch the model according to a certain 
        membrane voltage and time : 
            1 : initialization of gate variables for each channel 
            2 : calculation of currents for each ion
            3 : calculation of new states for each ion channel 
        """
        self.setGatingVar(self.Vm)
        self.updateCurrents(membraneVoltage, time)
        self.updateGate(time)
        

    
class Simulation : 

    def __init__(self, model):
        """
        Initialization of the simulation 
        """
        self.model = model
        self.createArrays(0, 0)
        

    def createArrays(self, nbPoints, time):
        """
        Arrays 
        -----------
        Creation of a empty table for each parameter to store the values 
        according to the time. The size of the tables is the number of points
        we want to observe on. 
        """
        self.times = np.arange(nbPoints) * time
        self.Vm, self.ILeak = np.empty(nbPoints),np.empty(nbPoints)
        self.INa, self.IK = np.empty(nbPoints), np.empty(nbPoints)
        self.n_state, self.m_state, self.h_state = np.empty(nbPoints),\
            np.empty(nbPoints),np.empty(nbPoints)
    
    def runSimulation(self, membraneVoltage, stepMs):
        """
        Calculations
        -----------
        Calculation of each value of the current and opening or closing 
        parameters for each channels according to the fchanging membrane 
        voltage and time. 
        """
        self.createArrays(len(membraneVoltage), stepMs)
        points_number = str(len(membraneVoltage))
        print("Time points simulation : "+ points_number)
        for i in range(len(membraneVoltage)):
            self.model.runModel(membraneVoltage[i], stepMs)
            self.Vm[i] = self.model.Vm
            self.INa[i] = self.model.INa
            self.IK[i] = self.model.IK
            self.ILeak[i] = self.model.ILeak
            self.h_state[i] = self.model.h.f
            self.m_state[i] = self.model.m.f
            self.n_state[i] = self.model.n.f
        print("simulation completed")
        
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


plt.tight_layout()
plt.show()





    