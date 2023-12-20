from Element import Element

class Process(Element):
    def __init__(self, name, delayMean, delayDev):
        super().__init__(name, delayMean, delayDev)

    def inAct(self):
        self.state = 1
        self.tnext = self.tcurr + super().getDelay()
        if(self.itemBlock!=None):
            self.itemBlock.UnBlock()
            #print(f"{self.itemBlock.name} працює")
        #print(f"'{self.name}' отримала вимогу, вже обробених: {self.quantity}, час: {self.tcurr}")

    def outAct(self):
        super().outAct()
        self.tnext = float("inf")
        if(self.state==-2):
            self.state = -1
        else:
            self.state = 0
        if(self.itemBlock!=None):
            self.itemBlock.Block()
            #print(f"{self.itemBlock.name} не працює")
        if(self.nextElement!=None):
            self.nextElement.inAct()
        #print(f"'{self.name}' передав вимогу, вже обробених: {self.quantity}, час: {self.tcurr}")

    def Block(self):
        if(self.state == 1 and self.nextElementBlock!=None):
            self.nextElementBlock.inAct()
            self.quantBlock+=1
            self.tnext = float("inf")
            #print(f"{self.name} отримав збій, кількість збоїв: {self.quantBlock}")
        elif(self.state == 1):
            self.state = -2
        else:
            self.state = -1
    
    def UnBlock(self):
        self.state = 0
