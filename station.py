class Station:
    agents = []

    def __init__(self,name):
        self.name = name
        self.next = {}
        self.previous = {}

    def defineNext(self,nextStation,line_id):
        self.next[line_id] = nextStation

    def definePrevious(self, previousStation,line_id):
        self.previous[line_id] = previousStation

    def addAgent(self, agent):
        self.agents.append(agent)

    def getNextFromLine(self, line_id,metro):
        if metro.forward == True:
            if self.next:
                return self.next[line_id]
            else:
                metro.forward = False
                return self.previous[line_id]
        else:
            if self.previous:
                return self.previous[line_id]
            else:
                metro.forward = True
                return self.next[line_id]