import numpy as np
from Process import Process
from System import System

class Model:
    def __init__(self, systems):
        self.list = systems
        self.event = [0,0]
        self.tnext = 0.0
        self.tcurr = 0.0

    def simulate(self, time):
        while self.tcurr < time:
            self.tnext = float('inf')

            for syst in self.list:
                syst.Active()
            
            for ind, syst in enumerate(self.list):
                for ind2, proc in enumerate(syst.processes):
                    tnextValue = np.min(proc.tnext)
                    if tnextValue < self.tnext and proc.state == 1 or proc.state ==-2:
                        self.tnext = tnextValue
                        self.event = [ind, ind2]

            self.tcurr = self.tnext
            for item in self.list:
                for item2 in item.processes:
                    item2.tcurr = self.tcurr

            self.list[self.event[0]].processes[self.event[1]].outAct()
