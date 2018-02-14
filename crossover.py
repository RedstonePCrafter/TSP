from random import randint
def crossover(parent1,parent2):
        child = Tour()

        startPos = randint(0,parent1.getTourSize())
        endPos = randint(0,parent1.getTourSize())

        for i in range(parent1.getTourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setStadt(i, parent1.getStadt(i))
            elif startPos > endPos:
                if not i < startPos and i > endPos:
                    child.setStadt(i, parent1.getStadt(i))

        for i in range(parent2.getTourSize()):
            if not child.istStadtvorhanden(parent2.getStadt(i)):
                for ii in range(parent1.getTourSize()):
                    if child.getStadt(ii) == null:
                        child.setCity(ii, parent2.getCity(i))
                        child.setStadt(ii,parent2.getStadt(i))
                        break
        return child
