from tour import Tour
from stadt import Stadt
from quicksort import quicksort
from quicksort import compare_fitness
from random import randint
from copy import deepcopy
class Tourlist(object):
    def __init__(self,tourcount,stadtcount):
        self.tourlist=[]
        self.stadtlist=[]
        self.stadtcount=stadtcount
        self.createStadtlist()
        self.minDist()
        self.maxDist()
        self.minTour=self.minDist()
        self.maxTour=self.maxDist()
        for i in range(tourcount):
            self.addTour(Tour(self.stadtlist))
        #neu
        print(self.fitness())

    def addTour(self,tour):
        self.tourlist.append(tour)
    def createStadtlist(self):
        stadtlist=[]
        for a in range(self.stadtcount):
            self.stadtlist.append(Stadt())

    def mutiere(self):
        for i in self.tourlist:
            i.mutieren()
	#neu Sonja 1.2
    def sort(self):
        self.tourlist= quicksort(self.tourlist,compare_fitness)
     #neu Sonja 1.2
    def getTour(self,position):
        return self.tourlist[position]

    #Mats&Daniel
    def minDist(self):
        minTour=0
        slist=self.stadtlist
        for stadt in slist:
            mindist=1500
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if mindist > Dist :
                         mindist= Dist
            minTour=minTour +mindist

        return minTour

    def maxDist(self):

        maxTour=0
        slist=self.stadtlist
        for stadt in slist:
            maxdist=0
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if maxdist < Dist :
                         maxdist= Dist
            maxTour=maxTour +maxdist

        return maxTour

    """von Daniel K. und Mats / Schranken zum ausrechnen der Fitness"""
    def Schranken(self):
        maxTour=0
        minTour=0
        slist=self.stadtlist
        for stadt in slist:
            mindist=1500
            maxdist=0
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if mindist > Dist :
                         mindist= Dist
                   if maxdist < Dist :
                         maxdist= Dist
            minTour=minTour +mindist
            maxTour=maxTour +maxdist

        return maxTour,minTour
    #neu Mats&Daniel
    def fitness(self):
        fitList=[]
        for tour in self.tourlist:
            #print(tour.laenge)
            fitList.append(tour.laenge/self.maxDist())
        return fitList






def crossover(parent1,parent2):
        child = Tour(deepcopy(parent1.liste))
        for i in range(child.getTourSize()):
            child.setStadt(None,i )

        startPos = randint(0,parent1.getTourSize()-1)
        endPos = randint(0,parent1.getTourSize()-1)

        for i in range(parent1.getTourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setStadt(parent1.getStadt(i),i)
            elif startPos > endPos:
                if not i < startPos and i > endPos:
                    child.setStadt(parent1.getStadt(i),i)
        for i in range(parent2.getTourSize()):
            if not child.istStadtvorhanden(parent2.getStadt(i)):
                for ii in range(parent1.getTourSize()):
                    if child.getStadt(ii) == None:
                        child.setStadt(parent2.getStadt(i),ii)
                        break
        print(parent1.getTourSize(),child.getTourSize(),parent2.getTourSize())
        for a in range(child.getTourSize()-1):
            print(a)
            print(child.getTourSize()-1)
            print(child.getStadt(a))
            print(parent1.getStadt(a))
            print(parent2.getStadt(a))
        return child


'''
t =Tourlist(100,20)
p1=t.tourlist[0]
p2=t.tourlist[1]
child=crossover(p1,p2)
print(p1.getLaenge())
print(p2.getLaenge())
print(child.getLaenge())
'''
#Jan's Befehle
"""
s1=Stadt()
s2=Stadt()
s3=Stadt()
s4=Stadt()
s5=Stadt()
s6=Stadt()
s1.x=1
s1.y=1
s2.x=2
s2.y=2
s3.x=3
s3.y=3
s4.x=4
s4.y=4
s5.x=5
s5.y=5
s6.x=6
s6.y=6
liste1=[s1,s2,s3,s4,s5,s6]
liste2=[s6,s5,s4,s3,s2,s1]
t1=Tour(liste1)
t2=Tour(liste2)
for s in t1.liste:
    print( s.getXY(),end='')
print()
for s in t2.liste:
    print( s.getXY(),end='')
print()
t3=crossover(t1,t2)
for s in t1.liste:
    print( s.getXY(),end='')
print()
for s in t2.liste:
    print( s.getXY(),end='')
print()
for s in t3.liste:
    print( s.getXY(),end='')
print()
"""

#Daniel K. und Mats Befehle
"""
t =Tourlist(100,20)
print(quicksort(t.tourlist,compare_fitness)[0].laenge)

#t =Tourlist(100,20)
#p1=t.tourlist[0]
#p2=t.tourlist[1]
#crossover(p1,p2)
"""

