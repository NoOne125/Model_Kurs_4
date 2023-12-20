class System:

    def __init__(self, processes, queue, maxqueue):
        self.processes = processes
        self.queue = queue
        self.maxqueue = maxqueue
 
    def inAct(self):
        self.queue+=1
        if(self.maxqueue<self.queue and self.maxqueue!=0):
            self.queue=self.maxqueue
        self.Active()

    def Active(self):
        if(self.queue == 0):
            return
        for proc in self.processes:
            if proc.state == 0:
                self.queue-=1
                #print(f"Черга передала '{proc.name}' вимогу, вимог в черзі: {self.queue}, час: {self.processes[0].tcurr}")
                proc.inAct()
                if(self.maxqueue==0):
                    self.queue = 0
                if(self.queue==0):
                    break

                
