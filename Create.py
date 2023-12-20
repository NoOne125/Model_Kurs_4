from Element import Element

class Create(Element):
    def __init__(self,name, delayMean, delayDev):
        super().__init__(name, delayMean, delayDev)
        self.state = 1

    def outAct(self):
        super().outAct()
        self.tnext = self.tcurr + super().getDelay()
        #print(f"'{self.name}' надіслав повідомлення, вже надісланних: {self.quantity}, час: {self.tcurr}")
        self.nextElement.inAct()
