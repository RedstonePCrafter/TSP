class Tourmanager(object):
    def __init__(self):
        self.liste=[]

    def addStadt(self,stadt):
        self.liste.append(stadt)

    def getTour(self):
        return self.liste
