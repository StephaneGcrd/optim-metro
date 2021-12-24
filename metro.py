class Metro:
    agents = []
    distanceToNext= 4
    notMovedSince=1
    
    def __init__(self,lineId, position):
        self.lineId =  lineId
        self.position = position
        self.forward = True

    def goToNext(self):
        difference = self.distanceToNext - self.notMovedSince

        if difference == 0:
            self.notMovedSince = 1
            self.position = self.position.getNextFromLine(self.lineId, self)
            print("Stopped.")
            print("Arrived to {} !".format(self.position.name))
        else:
            print("In transit !")
            self.notMovedSince += 1
            print("Distance to next : {}".format(difference))

    def addAgent(self, agent):
        self.agents.append(agent)

    def pickAgents(self):
        print(self.position.name)
        if len(self.position.agents)>0:
            print(self.position.agents)