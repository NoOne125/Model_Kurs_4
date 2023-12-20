import random

class Element:
    staticNextId = 0

    def __init__(self, name, delayMean, delayDev):
        self.name = name
        self.delayMean = delayMean
        self.delayDev = delayDev
        self.tnext = 0.
        self.quantity = 0
        self.tcurr = 0.
        self.state = 0
        self.nextElement = None
        self.itemBlock = None
        self.nextElementBlock = None
        self.quantBlock = 0
        self.SumDelay = 0
        self.N_delay=0

    def getDelay(self):
        result = random.random()
        result = self.delayMean - self.delayDev + 2 * result * self.delayDev
        self.SumDelay+=result
        self.N_delay+=1
        return result

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
    
    def set_tnext(self, value):
        self.tnext = value

    def get_tnext(self):
        return self.tnext
    
    def set_tcurr(self, value):
        self.tcurr = value

    def get_tcurr(self):
        return self.tcurr

    def inAct(self):
        pass

    def outAct(self):
        self.quantity+=1

    def TheorPract(self):
        print(f"Час {self.name}")
        print(f"Теоретична = {self.delayMean} +- {self.delayDev}")
        print(f"Практична = {self.SumDelay / self.N_delay}\n")
