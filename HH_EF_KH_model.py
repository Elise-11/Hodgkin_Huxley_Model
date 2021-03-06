#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabre
"""

"""
Terminology 
----------
NA = sodium ions
K = potassium ions
L = Leak (leakage current ions)
"""

import numpy as np
from scipy.integrate import odeint

class Gate:
    """
    The Gate class contains the functions related to the state of the open 
    or closed channels which depends on the time and is controlled by the 
    gating variable f, which follows the following differential equation: 
        df/dt = αf (1-f) - ßf(f)
    the channel opens for: 
        dα/dt = α (1-f)
    the channel closes for : 
        dß/dt = ß(f)
    so df/dt = dα/dt - dß/dt * time
    """
    #initialization of variables to 0 
    alpha = 0
    beta = 0
    f = 0

    #update gating variable 
    def update(self,time):
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
        #equa dif propotion de canaux ouverts 
        self.f += time * (alphaRate - betaRate)

    
    def inifiniteGateState(self):
        #propotion of open channels = opening channels / total channels
        self.f = self.alpha / (self.alpha + self.beta)
        


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
        self.m.inifiniteGateState()
        self.n.inifiniteGateState()
        self.n.inifiniteGateState()


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
        self.INa = np.power(self.m.f, 3) * self.gNa * self.h.f*(self.Vm-self.ENa)
        self.IK = np.power(self.n.f, 4) * self.gK * (self.Vm-self.EK)
        self.ILeak = self.gLeak * (self.Vm-self.ELeak)
        Isum = membraneVoltage - self.INa - self.IK - self.ILeak
        self.Vm += time * Isum / self.Cm
        

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
        






    