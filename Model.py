class Model:
    def __init__(self, systems):
        self.list = systems
        self.avgfreq = []
        self.avgfreq_time = []
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
                    tnextValue = proc.tnext
                    if tnextValue < self.tnext and proc.state == 1 or proc.state ==-2:
                        self.tnext = tnextValue
                        self.event = [ind, ind2]

            self.tcurr = self.tnext
            for item in self.list:
                for item2 in item.processes:
                    item2.tcurr = self.tcurr

            self.list[self.event[0]].processes[self.event[1]].outAct()
            self.avgfreq.append(self.list[1].processes[0].quantBlock/self.list[0].processes[0].quantity)
            self.avgfreq_time.append(self.tcurr)
