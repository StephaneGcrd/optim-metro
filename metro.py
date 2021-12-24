class Metro:
    agents = []
    
    def __init__(self,lineId, position):
        self.lineId =  lineId
        self.position = position
        self.forward = True

    def goToNext(self):
        self.position = self.position.getNextFromLine(self.lineId, self)

    def addAgent(self, agent):
        self.agents.append(agent)

    def pickAgents(self):
        print(self.position.name)
        if len(self.position.agents)>0:
            print(self.position.agents)